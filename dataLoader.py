import json
import pandas as pd
import numpy as np

import statUtils

from collections import defaultdict
def load_data_event(event):
    # load saved data (make sure to download w/ downloadData.py)
    with open(f"data/{event}.json", 'r') as f:
        json_data = json.load(f)

    matches = json_data['matches']
    unplayed_matches = json_data['unplayed_matches']
    oprs = json_data['oprs']
    teams = json_data['teams']

    # parse into pandas dataframe
    def flatten_data_matches(matches, played=True):
        data_dict = defaultdict(list)

        data_dict['match_key'] == []
        data_dict['match_type'] == []
        data_dict['match_number'] == []

        data_dict['red_1_key'] == []
        data_dict['red_2_key'] == []
        data_dict['red_3_key'] == []
        data_dict['red_keys'] == []

        data_dict['blue_1_key'] == []
        data_dict['blue_2_key'] == []
        data_dict['blue_3_key'] == []
        data_dict['blue_keys'] == []

        for match in matches:
            match_data = matches[match]
            
            data_dict['match_key'].append(match_data['key'])
            data_dict['match_type'].append(match_data['match_type'])
            data_dict['match_number'].append(match_data['number'])

            for alliance_color in ['blue', 'red']:
                alliance_data = match_data['alliances'][alliance_color]
                for robot_num, robot_key in enumerate(alliance_data['team_keys']):
                    data_dict[f"{alliance_color}_{robot_num+1}_key"].append(robot_key)
                data_dict[f"{alliance_color}_keys"].append(alliance_data['team_keys'])
                
                if played:
                    score_breakdown = alliance_data['score_breakdown']
                    
                    data_dict[f"{alliance_color}_foul_count"].append(score_breakdown['foul_count'])
                    data_dict[f"{alliance_color}_points_scored"].append(score_breakdown['points_scored'])
                    data_dict[f"{alliance_color}_rp"].append(score_breakdown['rp'])
                    data_dict[f"{alliance_color}_cargo_rp"].append(score_breakdown['rp_breakdown']['cargo_achieved'])
                    data_dict[f"{alliance_color}_hangar_rp"].append(score_breakdown['rp_breakdown']['hangar_achieved'])
                    
                    for robot_num, taxi_points in enumerate(score_breakdown['taxis']):
                        data_dict[f"{alliance_color}_{robot_num+1}_taxi"].append(taxi_points)
                    for robot_num, endgame_points in enumerate(score_breakdown['endgames']):
                        data_dict[f"{alliance_color}_{robot_num+1}_endgame"].append(endgame_points)
                    
                    for cargo_placement in ['lower', 'upper']:
                        for opmode in ['auto', 'teleop']:
                            data_dict[f"{alliance_color}_cargo_{cargo_placement}_{opmode}"].append(score_breakdown['cargo'][cargo_placement][opmode])
                
        df = pd.DataFrame(data=data_dict)
        return df

    def get_match_team_data_breakdown(match_data, alliance_color):
        return [
            match_data[f'{alliance_color}_points_scored'],
            match_data[f'{alliance_color}_cargo_lower_auto'],
            match_data[f'{alliance_color}_cargo_lower_teleop'],
            match_data[f'{alliance_color}_cargo_upper_auto'],
            match_data[f'{alliance_color}_cargo_upper_teleop']
        ]

    # get team data (like opr) into a dataframe
    def get_feature(team_key, data, feature_name):
        return data.loc[data['team_key'] == team_key][feature_name]

    # per component OPR
    # thanks to [this](https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/)
    def calculate_oprs(point_objective):
        match_matrix = np.zeros((len(qualification_matches)*2, len(teams)))
        score_matrix = np.zeros((len(qualification_matches)*2, 1))

        for _, match in qualification_matches.iterrows():
            i = match['match_number']-1
            for red_team in match['red_keys']:
                match_matrix[i*2][teams.index(red_team)] = 1
            score_matrix[i*2][0] = match[f'red_{point_objective}']

            for blue_team in match['blue_keys']:
                match_matrix[i*2+1][teams.index(blue_team)] = 1
            score_matrix[i*2+1][0] = match[f'blue_{point_objective}']

        left_matrix = match_matrix.T.dot(match_matrix)
        right_matrix = match_matrix.T.dot(score_matrix)
        opr_matrix = np.linalg.pinv(left_matrix).dot(right_matrix)
        return opr_matrix

    all_match_data = flatten_data_matches(matches)
    qualification_matches = all_match_data.loc[all_match_data['match_type'] == 'qm']

    all_unplayed_matches = flatten_data_matches(unplayed_matches, played=False)
    qualification_matches_unplayed = all_unplayed_matches.loc[all_unplayed_matches['match_type'] == 'qm']

    # get team scores into a dataframe
    team_scores = []
    for _, match in qualification_matches.iterrows():
        for i, team in enumerate(match['blue_keys']):
            team_scores.append(
                [team] + get_match_team_data_breakdown(match, 'blue') + [match[f'blue_{i+1}_endgame']] + [match['match_number']]
            )
        for i, team in enumerate(match['red_keys']):
            team_scores.append(
                [team] + get_match_team_data_breakdown(match, 'red') + [match[f'red_{i+1}_endgame']] + [match['match_number']]
            )
    team_scores = pd.DataFrame(team_scores, columns=['team_key', 'team_score', 'lower_auto_cargo', 'lower_teleop_cargo', 'upper_auto_cargo', 'upper_teleop_cargo', 'endgame', 'match_number'])
    team_scores = team_scores.sort_values(by=['team_key'])

    # get generic team data into a dataframe
    team_data = []
    for team in teams:
        team_data.append([
            team,
            oprs.get(team, 0),
            np.mean(get_feature(team, team_scores, 'team_score')),
            np.mean(get_feature(team, team_scores, 'lower_auto_cargo')),
            np.mean(get_feature(team, team_scores, 'lower_teleop_cargo')),
            np.mean(get_feature(team, team_scores, 'upper_auto_cargo')),
            np.mean(get_feature(team, team_scores, 'upper_teleop_cargo')),
            np.mean(get_feature(team, team_scores, 'endgame'))
        ])
    team_data = pd.DataFrame(team_data, columns=['team_key', 'opr', 'mean_score', 'mean_lower_auto_cargo', 'mean_lower_teleop_cargo', 'mean_upper_auto_cargo', 'mean_upper_teleop_cargo', 'mean_endgame'])
    team_data.sort_values(by=['mean_score'])

    opr_features = ['points_scored', 'cargo_lower_auto', 'cargo_lower_teleop', 'cargo_upper_auto', 'cargo_upper_teleop']

    # get component opr into a dataframe
    team_component_opr_data = []
    for i, team in enumerate(teams):
        adding = [team, team_scores.loc[team_scores['team_key'] == team].shape[0]]
        for feature in opr_features:
            opr_prediction, std = statUtils.residual_team(team, qualification_matches, teams, feature)
            adding += [opr_prediction, std]
        adding += [
            team_data.loc[team_data['team_key'] == team].iloc[0]['mean_endgame'],
            team_data.loc[team_data['team_key'] == team].iloc[0]['mean_score']
        ]

        team_component_opr_data.append(adding)

    column_names = ['team_key', 'matches_played']
    for i in opr_features:
        column_names += [f'{i}', f'{i}_std']
    column_names += ['mean_endgame', 'mean_score']

    team_component_opr_data = pd.DataFrame(team_component_opr_data, columns=column_names)
    team_component_opr_data.sort_values(by='points_scored')

    return qualification_matches, qualification_matches_unplayed, team_scores, team_data, team_component_opr_data

def normalize_opr(i):
    # helper functionto normalize OPRs to point values
    team_component_opr_normalized = i.copy(deep=True)
    team_component_opr_normalized['cargo_lower_auto'] *= 2
    team_component_opr_normalized['cargo_lower_teleop'] *= 1
    team_component_opr_normalized['cargo_upper_auto'] *= 4
    team_component_opr_normalized['cargo_upper_teleop'] *= 2
    return team_component_opr_normalized