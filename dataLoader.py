import json
import pandas as pd
import numpy as np

from collections import defaultdict
def load_data_event(event):
    # load saved data (make sure to download w/ downloadData.py)
    with open(f"data/{event}.json", 'r') as f:
        json_data = json.load(f)

    matches = json_data['matches']
    oprs = json_data['oprs']
    teams = json_data['teams']

    # parse into pandas dataframe
    def flatten_data_matches(json_data):
        data_dict = defaultdict(list)

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
                
                score_breakdown = alliance_data['score_breakdown']
                
                data_dict[f"{alliance_color}_endgame_level"].append(score_breakdown['endgame_level'])
                data_dict[f"{alliance_color}_foul_count"].append(score_breakdown['foul_count'])
                data_dict[f"{alliance_color}_points_scored"].append(score_breakdown['points_scored'])
                data_dict[f"{alliance_color}_max_stage"].append(score_breakdown['max_stage'])
                data_dict[f"{alliance_color}_hang_rp"].append(score_breakdown['rp']['shield_operational'])
                data_dict[f"{alliance_color}_wheel_rp"].append(score_breakdown['rp']['shield_energized'])
                
                for robot_num, init_line_points in enumerate(score_breakdown['init_lines']):
                    data_dict[f"{alliance_color}_{robot_num+1}_init_line"].append(init_line_points)
                for robot_num, endgame_points in enumerate(score_breakdown['endgames']):
                    data_dict[f"{alliance_color}_{robot_num+1}_endgame"].append(endgame_points)
                
                for cell_placement in ['bottom', 'outer', 'inner']:
                    for opmode in ['auto', 'teleop']:
                        data_dict[f"{alliance_color}_cells_{cell_placement}_{opmode}"].append(score_breakdown['cells'][cell_placement][opmode])
                
        df = pd.DataFrame(data=data_dict)
        return df

    def get_match_team_data_breakdown(match_data, alliance_color):
        return [
            match_data[f'{alliance_color}_points_scored'],
            match_data[f'{alliance_color}_cells_bottom_auto'],
            match_data[f'{alliance_color}_cells_bottom_teleop'],
            match_data[f'{alliance_color}_cells_outer_auto'],
            match_data[f'{alliance_color}_cells_outer_teleop'],
            match_data[f'{alliance_color}_cells_inner_auto'],
            match_data[f'{alliance_color}_cells_inner_teleop']
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

    all_match_data = flatten_data_matches(json_data)
    qualification_matches = all_match_data.loc[all_match_data['match_type'] == 'qm']

    # get team scores into a dataframe
    team_scores = []
    for _, match in qualification_matches.iterrows():
        for team in match['blue_keys']:
            team_scores.append([team] + get_match_team_data_breakdown(match, 'blue'))
        for team in match['red_keys']:
            team_scores.append([team] + get_match_team_data_breakdown(match, 'red'))
    team_scores = pd.DataFrame(team_scores, columns=['team_key', 'team_score', 'bottom_auto_cells', 'bottom_teleop_cells', 'outer_auto_cells', 'outer_teleop_cells', 'inner_auto_cells', 'inner_teleop_cells'])
    team_scores = team_scores.sort_values(by=['team_key'])

    # get generic team data into a dataframe
    team_data = []
    for team in teams:
        team_data.append([
            team,
            oprs.get(team, 0),
            np.mean(get_feature(team, team_scores, 'team_score')),
            np.mean(get_feature(team, team_scores, 'bottom_auto_cells')),
            np.mean(get_feature(team, team_scores, 'bottom_teleop_cells')),
            np.mean(get_feature(team, team_scores, 'outer_auto_cells')),
            np.mean(get_feature(team, team_scores, 'outer_teleop_cells')),
            np.mean(get_feature(team, team_scores, 'inner_auto_cells')),
            np.mean(get_feature(team, team_scores, 'inner_teleop_cells')),
        ])
    team_data = pd.DataFrame(team_data, columns=['team_key', 'opr', 'mean_score', 'mean_bottom_auto_cells', 'mean_bottom_teleop_cells', 'mean_outer_auto_cells', 'mean_outer_teleop_cells', 'mean_inner_auto_cells', 'mean_inner_teleop_cells'])
    team_data.sort_values(by=['mean_score'])

    # get component opr into a dataframe
    team_component_opr_data = []
    for i, team in enumerate(teams):
        team_component_opr_data.append([
            team,
            calculate_oprs('points_scored')[i][0],
            calculate_oprs('cells_bottom_auto')[i][0],
            calculate_oprs('cells_bottom_teleop')[i][0],
            calculate_oprs('cells_inner_auto')[i][0],
            calculate_oprs('cells_inner_teleop')[i][0],
            calculate_oprs('cells_outer_auto')[i][0],
            calculate_oprs('cells_outer_teleop')[i][0],
            team_data.loc[team_data['team_key'] == team].iloc[0]['mean_score']
        ])
    team_component_opr_data = pd.DataFrame(team_component_opr_data, columns=['team_key', 'points_scored', 'cells_bottom_auto', 'cells_bottom_teleop', 'cells_inner_auto', 'cells_inner_teleop', 'cells_outer_auto', 'cells_outer_teleop', 'mean_score'])
    team_component_opr_data.sort_values(by='points_scored')

    return qualification_matches, team_scores, team_data, team_component_opr_data