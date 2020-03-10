from sklearn import linear_model
import numpy as np
import pandas as pd

import math

def nan_in_list(l):
    for i in l:
        if math.isnan(i):
            return True
    return False

def perform_regression(data, features, target):
    reg = linear_model.LinearRegression()
    x = []
    y = []

    for _, data_row in data.iterrows():
        x_adding = [data_row[i] for i in features]
        y_adding = data_row[target]
        if not nan_in_list(x_adding) and not nan_in_list([y_adding]):
            x.append(x_adding)
            y.append(y_adding)
    reg.fit(x, y)

    return reg, reg.score(x, y)

# common function for calculating a team's OPR given a point objective to get the OPR for and matches to look at
# still, thanks to [this](https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/)
def calculate_oprs(matches, team_keys, point_objective):
    match_matrix = np.zeros((len(matches)*2, len(team_keys)))
    score_matrix = np.zeros((len(matches)*2, 1))

    i = 0
    for _, match in matches.iterrows():
        for red_team in match['red_keys']:
            match_matrix[i*2][team_keys.index(red_team)] = 1
        score_matrix[i*2][0] = match[f'red_{point_objective}']

        for blue_team in match['blue_keys']:
            match_matrix[i*2+1][team_keys.index(blue_team)] = 1
        score_matrix[i*2+1][0] = match[f'blue_{point_objective}']

        i += 1

    l_matrix = match_matrix.T.dot(match_matrix)
    r_matrix = match_matrix.T.dot(score_matrix)
    opr_matrix = np.linalg.pinv(l_matrix).dot(r_matrix)

    return opr_matrix

# to implement wgardner's method, we'll need to iterate through teams and compute OPR while taking out matches that they're in
def wgardner_team(team, matches, team_keys, point_objective):
    # first get matches that the team is in {O(n)}
    matches_playing = []
    for i, match in matches.iterrows():
        if team in match['red_keys'] or team in match['blue_keys']:
            matches_playing.append(i)

    # iterate through the matches, calculate OPR w/out that match being considered
    oprs = []
    for match_removing in matches_playing:
        oprs.append(calculate_oprs(matches.drop(match_removing), team_keys, point_objective)[team_keys.index(team)][0])

    # take the mean and standard deviation
    std = np.std(oprs)
    mean = np.mean(oprs)

    return mean, std

# for the math approach, we iterate through the matches that a team plays with initial OPR predictions, find the residual, and then use that in our error stuff
def residual_team(team, matches, team_keys, point_objective):
    # get initial OPR results
    opr_predictions_initial = calculate_oprs(matches, team_keys, point_objective)

    # go through and find residuals on a per match basis
    predictions = []
    targets = []
    for _, match in matches.iterrows():
        alliance_keys = observed_score = None
        if team in match['red_keys']:
            alliance_keys = match['red_keys']
            observed_score = match[f'red_{point_objective}']
        if team in match['blue_keys']:
            aliance_keys = match['blue_keys']
            observed_score = match[f'blue_{point_objective}']
        
        if alliance_keys != None:
            predictions.append(sum([
                opr_predictions_initial[team_keys.index(key)][0] for key in alliance_keys
            ]))
            targets.append(observed_score)
    predictions = np.array(predictions)
    targets = np.array(targets)

    # calculate std from residuals
    std = np.sqrt(np.mean((predictions-targets)**2))

    return opr_predictions_initial[team_keys.index(team)][0], std

# get a dataframe with the new OPR calculations
def get_opr_std_method(matches, team_keys, point_objective, opr_function):
    team_opr_data = []
    for team in team_keys:
        mean, std = opr_function(team, qualification_matches, team_keys, point_objective)
        team_opr_data.append([team, mean, std])
    return pd.DataFrame(team_opr_data, columns=['team_key', 'opr_mean', 'opr_std'])