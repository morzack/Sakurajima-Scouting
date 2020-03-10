# classes and things used to construct and run the statistical modelling stuff that I've developed

import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

import json
import math

from os import listdir
from os.path import isfile, join

from dataLoader import load_data_event
from statUtils import perform_regression

sns.set_style('whitegrid')

# custom score prediction model that uses distributions
class ScorePredictor:
    def __init__(self, features_in=[], oprs=[], loading_file=''):
        if loading_file == '':
            self.features_in = features_in
            self._build_model(oprs)
        else:
            self.load_model(loading_file)

    def _build_model(self, oprs):
        full_feature_regression, self.r2 = perform_regression(oprs, self.features_in, 'mean_score')
        self.reg_coef = {f: full_feature_regression.coef_[i] for i, f in enumerate(self.features_in)}
        self.reg_coef = {k: v for k, v in sorted(self.reg_coef.items(), key=lambda i: i[1])}
        self.intercept = full_feature_regression.intercept_
        self.n_trained = oprs.shape[0]

    def save_model(self, filename):
        with open(filename, 'w') as f:
            json.dump({
            'r2': self.r2,
            'reg_coef': self.reg_coef,
            'intercept': self.intercept,
            'n_trained': self.n_trained,
            'features_in': self.features_in
        }, f)

    def load_model(self, filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        self.r2 = json_data['r2']
        self.reg_coef = json_data['reg_coef']
        self.intercept = json_data['intercept']
        self.n_trained = json_data['n_trained']
        self.features_in = json_data['features_in']

    def _get_prediction_values(self, team_key, oprs):
        mean_outputs = []
        deviations = []
        team_oprs = oprs.loc[oprs['team_key'] == team_key].iloc[-1]
        for feature in self.features_in:
            mean_outputs.append(team_oprs[feature] * self.reg_coef[feature])
            if f'{feature}_std' in team_oprs:
                deviations.append(team_oprs[f'{feature}_std'] * self.reg_coef[feature])
        mean_outputs = np.array(mean_outputs)
        deviations = np.array(deviations)
    
        predicted_score_mean = np.sum(mean_outputs) + self.intercept
        predicted_score_deviation = np.sqrt(np.sum(deviations**2))
    
        return predicted_score_mean, predicted_score_deviation
    
    def predict_team(self, team_key, confidence, oprs, team_data):
        mean, std = self._get_prediction_values(team_key, oprs)
        n = oprs.loc[oprs['team_key'] == team_key].iloc[-1]['matches_played']
        t_value = stats.t.ppf(confidence, n)
        se = math.sqrt(
            ((n+1) * std**2 + (mean - team_data.loc[team_data['team_key'] == team_key].iloc[-1]['mean_score'])**2)
            /n
        )
        interval = t_value*se
        return mean, interval
    
    def predict_alliance(self, team_keys, confidence, oprs, team_data):
        means = []
        stds = []
        for team in team_keys:
            team_mean, team_std = self._get_prediction_values(team, oprs)
            means.append(team_mean)
            stds.append(team_std)
        means, stds = np.array(means), np.array(stds)

        mean = np.mean(means)
        std = np.sqrt(np.sum(stds**2))

        n = 0
        mean_scores_observed = []
        for team in team_keys:
            n += oprs.loc[oprs['team_key'] == team].iloc[-1]['matches_played']
            mean_scores_observed.append(team_data.loc[team_data['team_key'] == team].iloc[-1]['mean_score'])
        mean_score_observed = np.mean(mean_scores_observed)
        t_value = stats.t.ppf(confidence, n)
        se = math.sqrt(
            ((n+1) * std**2 + (mean - mean_score_observed)**2)
            /n
        )
        interval = t_value*se
        return mean, interval

# scoring model with OPR loaded as well
class ScoreModelOpr:
    def __init__(self, score_model_file="", opr_file="", team_data_file="", score_model=None, oprs=None, team_data=None):
        if score_model_file != "":
            self.score_model = ScorePredictor(loading_file=score_model_file)
            self.oprs = pd.read_csv(opr_file)
            self.team_data = pd.read_csv(team_data_file)
        elif score_model != None:
            self.score_model = score_model
            self.oprs = oprs
            self.team_data = team_data
    
    def save(self, score_model_file="", opr_file="", team_data_file=""):
        if score_model_file != "":
            self.score_model.save_model(score_model_file)
        if opr_file != "":
            self.oprs.to_csv(opr_file)
        if team_data_file != "":
            self.team_data.to_csv(team_data_file)

    def predict_alliance_confidence(self, alliance_keys, confidence):
        mean, interval = self.score_model.predict_alliance(alliance_keys, confidence, self.oprs, self.team_data)
        return (mean-interval, mean+interval)
    
    def predict_team_confidence(self, team_key, confidence):
        mean, interval = self.score_model.predict_team(team_key, confidence, self.oprs, self.team_data)
        return (mean-interval, mean+interval)

    def estimate_match_victor(self, red_alliance_keys, blue_alliance_keys, confidence_bounds=(.5, .99), confidence_step=.01):
        # estimate the victor of a match and return how confident we are about the prediction
        # TODO make this a binary search to improve performance
        confidence = confidence_bounds[1]+confidence_step
        while confidence > confidence_bounds[0]:
            confidence -= confidence_step
            
            red_interval = self.predict_alliance_confidence(red_alliance_keys, confidence)
            blue_interval = self.predict_alliance_confidence(blue_alliance_keys, confidence)

            if not (
                (blue_interval[0] < red_interval[0] < blue_interval[1]) or (blue_interval[0] < red_interval[1] < blue_interval[1]) or
                (red_interval[0] < blue_interval[0] < red_interval[1]) or (red_interval[0] < blue_interval[1] < red_interval[1])
                ):
                break

        predicted_victor = 'red' if red_interval[0] > blue_interval[1] else 'blue'
        return predicted_victor, confidence

    def predict_scores_event(self, qualification_matches, confidence_bounds=(.5, .99), confidence_step=.01, feedback=False):
        # predict scores for matches at an event
        # note that when using feedback, this doesn't take penalties into account for the score.
        # this is a potentially fatal flaw with the model, but I haven't seen any issues so far.
        # i'd be willing to bet that accounting for penalties will bump up our r^2 value by a lot
        match_predictions = []
        for _, match in qualification_matches.iterrows():
            red_keys = [match['red_1_key'], match['red_2_key'], match['red_3_key']]
            blue_keys = [match['blue_1_key'], match['blue_2_key'], match['blue_3_key']]

            predicted_victor, confidence = self.estimate_match_victor(red_keys, blue_keys, confidence_bounds, confidence_step)

            adding = [match['match_number'], confidence, predicted_victor]
            if feedback:
                adding += ['red' if match['red_points_scored'] > match['blue_points_scored'] else 'blue']

            match_predictions.append(adding)
        columns = ['match_number', 'confidence', 'predicted_victor']
        if feedback:
            columns += ['actual_victor']
        return pd.DataFrame(match_predictions, columns=columns)

if __name__ == '__main__':
    score_model_complete = ScoreModelOpr(
        score_model_file="data/saved_models/v1/score-model.json",
        opr_file="data/saved_models/v1/opr-data.csv",
        team_data_file="data/saved_models/v1/team-data.csv"
    )

    print(score_model_complete.estimate_match_victor(
        ['frc5160', 'frc5511', 'frc7763'],
        ['frc6502', 'frc4561', 'frc5607']
    ))