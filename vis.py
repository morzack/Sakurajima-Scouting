import json
import math

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

from dataLoader import load_data_event
import modelling

sns.set()

primary_color = sns.xkcd_rgb['bluegreen']
secondary_color = sns.xkcd_rgb['coral']
background_color = sns.xkcd_rgb['white']

def get_matches_played(team_key, qualification_matches, team_scores):
    # get dataframes of score breakdowns and match data for matches a team is in
    match_nums = []
    for _, match in qualification_matches.iterrows():
        if team_key in [match['red_1_key'], match['red_2_key'], match['red_3_key'], match['blue_1_key'], match['blue_2_key'], match['blue_3_key']]:
            match_nums.append(match['match_number'])
    match_scores_played = team_scores.loc[team_scores['team_key'] == team_key]
    matches_played = qualification_matches.loc[qualification_matches['match_number'].isin(match_nums)]
    return match_scores_played, matches_played

def gen_team_summary(team_key, qualification_matches, team_scores, team_data, filename='plots/out.png', feature='team_score'):
    # this will generate a summary graph for the team key passed in
    # equivalent to last year's Sakurajima functionality
    match_scores_played, matches_played = get_matches_played(team_key, qualification_matches, team_scores)

    plt.figure(figsize=(10, 10), dpi=80)
    plt.suptitle(f'Performance summary of {feature} for {team_key}')

    # team performance across matches
    plt.subplot(2, 2, 1)
    sns.regplot(x='match_number', y=feature, data=match_scores_played, color=primary_color)
    plt.title(f'{feature} across Qualifier Matches for {team_key}')

    # "histogram" of scoring metrics
    plt.subplot(2, 2, 2)
    sns.kdeplot(match_scores_played[feature], shade=True, color=primary_color, label=f'{team_key}')
    sns.kdeplot(team_scores[feature], shade=True, color=secondary_color, label='Overall')
    plt.title(f'{feature} distribution for {team_key}')

    # boxplot of team performance
    plt.subplot(2, 2, 3)
    sns.boxplot(y=feature, color=primary_color, data=match_scores_played, width=.2)
    plt.title(f'{feature} distribution for {team_key}')

    # percentile/curve of feature
    plt.subplot(2, 2, 4)
    event_mean, event_std = np.mean(team_scores[feature]), np.std(team_scores[feature])
    team_data_key = 'mean_score' if feature == 'team_score' else f'mean_{feature}'
    event_percentiles = stats.norm.cdf((team_data[team_data_key] - event_mean) / event_std)
    percentile = stats.norm.cdf((np.mean(match_scores_played[feature]) - event_mean) / event_std)
    ax = sns.kdeplot(event_percentiles)
    line = ax.get_lines()[-1]
    x, y = line.get_data()
    mask = x < percentile
    x, y = x[mask], y[mask]
    ax.fill_between(x, y1=y, alpha=.5, facecolor=secondary_color)
    plt.title(f'Percentile plot of {feature} for {team_key}')

    plt.savefig(filename, bbox_inches='tight')

def predict_matches(score_prediction_model, team_key, qualification_matches, team_scores):
    # get a dataframe with match predictions
    _, matches_played = get_matches_played(team_key, qualification_matches, team_scores)
    predictions = score_prediction_model.predict_scores_event(matches_played)
    
    predicted_results_team = []
    for _, match in predictions.iterrows():
        qual_match_data = matches_played.loc[matches_played['match_number'] == match['match_number']].iloc[0]
        color = 'red' if team_key in [qual_match_data['red_1_key'], qual_match_data['red_2_key'], qual_match_data['red_3_key']] else 'blue'
        predicted_results_team.append([
            match['match_number'], modelling.get_probability(match['confidence']), 'win' if match['predicted_victor'] == color else 'lose'
        ])
    predicted_results_team = pd.DataFrame(predicted_results_team, columns=['match_num', 'probability', 'predicted_result'])
    predicted_results_team = predicted_results_team.sort_values('match_num')

    return predicted_results_team