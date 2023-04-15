import json
import pandas as pd
import numpy as np
import ast

import src.stat_utils as stat_utils

from collections import defaultdict


def get_feature(team_key, data, feature_name):
    return data.loc[data['team_key'] == team_key][feature_name]

# per component OPR
# thanks to [this](https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/)


def calculate_oprs(point_objective, qualification_matches, teams):
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


class DataLoader:
    def flatten_data_matches(self, matches, played=True):
        pass

    def get_match_team_data_breakdown(self, match_data, alliance_color):
        pass

    def normalize_opr(self, i):
        pass

    def load_data_event(self, event, data_root="data"):
        pass


class DataLoader2022(DataLoader):
    def flatten_data_matches(self, matches, played=True):
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
                    data_dict[f"{alliance_color}_{robot_num+1}_key"].append(
                        robot_key)
                data_dict[f"{alliance_color}_keys"].append(
                    alliance_data['team_keys'])

                if played:
                    score_breakdown = alliance_data['score_breakdown']

                    data_dict[f"{alliance_color}_foul_count"].append(
                        score_breakdown['foul_count'])
                    data_dict[f"{alliance_color}_points_scored"].append(
                        score_breakdown['points_scored'])
                    data_dict[f"{alliance_color}_rp"].append(
                        score_breakdown['rp'])
                    data_dict[f"{alliance_color}_cargo_rp"].append(
                        score_breakdown['rp_breakdown']['cargo_achieved'])
                    data_dict[f"{alliance_color}_hangar_rp"].append(
                        score_breakdown['rp_breakdown']['hangar_achieved'])

                    for robot_num, taxi_points in enumerate(score_breakdown['taxis']):
                        data_dict[f"{alliance_color}_{robot_num+1}_taxi"].append(
                            taxi_points)
                    for robot_num, endgame_points in enumerate(score_breakdown['endgames']):
                        data_dict[f"{alliance_color}_{robot_num+1}_endgame"].append(
                            endgame_points)

                    for cargo_placement in ['lower', 'upper']:
                        for opmode in ['auto', 'teleop']:
                            data_dict[f"{alliance_color}_cargo_{cargo_placement}_{opmode}"].append(
                                score_breakdown['cargo'][cargo_placement][opmode])

        df = pd.DataFrame(data=data_dict)
        return df

    def get_match_team_data_breakdown(self, match_data, alliance_color):
        return [
            match_data[f'{alliance_color}_points_scored'],
            match_data[f'{alliance_color}_cargo_lower_auto'],
            match_data[f'{alliance_color}_cargo_lower_teleop'],
            match_data[f'{alliance_color}_cargo_upper_auto'],
            match_data[f'{alliance_color}_cargo_upper_teleop']
        ]

    def normalize_opr(self, i):
        # helper functionto normalize OPRs to point values
        team_component_opr_normalized = i.copy(deep=True)
        team_component_opr_normalized['cargo_lower_auto'] *= 2
        team_component_opr_normalized['cargo_lower_teleop'] *= 1
        team_component_opr_normalized['cargo_upper_auto'] *= 4
        team_component_opr_normalized['cargo_upper_teleop'] *= 2
        return team_component_opr_normalized

    def load_data_event(self, event, data_root="data"):
        # load saved data (make sure to download w/ downloadData.py)
        with open(f"{data_root}/{event}.json", 'r') as f:
            json_data = json.load(f)

        matches = json_data['matches']
        unplayed_matches = json_data['unplayed_matches']
        oprs = json_data['oprs']
        teams = json_data['teams']

        all_match_data = self.flatten_data_matches(matches)
        qualification_matches = all_match_data.loc[all_match_data['match_type'] == 'qm']

        all_unplayed_matches = self.flatten_data_matches(
            unplayed_matches, played=False)
        qualification_matches_unplayed = all_unplayed_matches.loc[
            all_unplayed_matches['match_type'] == 'qm']

        # get team scores into a dataframe
        team_scores = []
        for _, match in qualification_matches.iterrows():
            for i, team in enumerate(match['blue_keys']):
                team_scores.append(
                    [team] + self.get_match_team_data_breakdown(match, 'blue') + [
                        match[f'blue_{i+1}_endgame']] + [match['match_number']]
                )
            for i, team in enumerate(match['red_keys']):
                team_scores.append(
                    [team] + self.get_match_team_data_breakdown(
                        match, 'red') + [match[f'red_{i+1}_endgame']] + [match['match_number']]
                )
        team_scores = pd.DataFrame(team_scores, columns=['team_key', 'team_score', 'lower_auto_cargo',
                                                         'lower_teleop_cargo', 'upper_auto_cargo', 'upper_teleop_cargo', 'endgame', 'match_number'])
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
                np.mean(get_feature(team, team_scores, 'endgame')),
                np.std(get_feature(team, team_scores, 'endgame'))
            ])
        team_data = pd.DataFrame(team_data, columns=['team_key', 'opr', 'mean_score', 'mean_lower_auto_cargo',
                                                     'mean_lower_teleop_cargo', 'mean_upper_auto_cargo', 'mean_upper_teleop_cargo', 'mean_endgame', 'mean_endgame_std'])
        team_data.sort_values(by=['mean_score'])

        opr_features = ['points_scored', 'cargo_lower_auto',
                        'cargo_lower_teleop', 'cargo_upper_auto', 'cargo_upper_teleop']

        # get component opr into a dataframe
        team_component_opr_data = []
        for i, team in enumerate(teams):
            adding = [
                team, team_scores.loc[team_scores['team_key'] == team].shape[0]]
            for feature in opr_features:
                opr_prediction, std = stat_utils.residual_team(
                    team, qualification_matches, teams, feature)
                adding += [opr_prediction, std]
            adding += [
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_endgame'],
                team_data.loc[team_data['team_key'] ==
                              team].iloc[0]['mean_endgame_std'],
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_score']
            ]

            team_component_opr_data.append(adding)

        column_names = ['team_key', 'matches_played']
        for i in opr_features:
            column_names += [f'{i}', f'{i}_std']
        column_names += ['mean_endgame', 'mean_endgame_std', 'mean_score']

        team_component_opr_data = pd.DataFrame(
            team_component_opr_data, columns=column_names)
        team_component_opr_data.sort_values(by='points_scored')

        return qualification_matches, qualification_matches_unplayed, team_scores, team_data, team_component_opr_data


class DataLoader2023(DataLoader):
    def __init__(self):
        self.opr_features = ['points_scored', 'piece_low_auto', 'piece_mid_auto',
                        'piece_high_auto', 'piece_low_teleop', 'piece_mid_teleop', 'piece_high_teleop']

    def flatten_data_matches(self, matches, played=True):
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
                    data_dict[f"{alliance_color}_{robot_num+1}_key"].append(
                        robot_key)
                data_dict[f"{alliance_color}_keys"].append(
                    alliance_data['team_keys'])

                if played:
                    score_breakdown = alliance_data['score_breakdown']

                    data_dict[f"{alliance_color}_foul_count"].append(
                        score_breakdown['foul_count'])
                    data_dict[f"{alliance_color}_points_scored"].append(
                        score_breakdown['points_scored'])
                    data_dict[f"{alliance_color}_rp"].append(
                        score_breakdown['rp'])
                    data_dict[f"{alliance_color}_coop_bonus"].append(
                        score_breakdown['coop_bonus'])
                    data_dict[f"{alliance_color}_sustainability_rp"].append(
                        score_breakdown['rp_breakdown']['sustainability'])
                    data_dict[f"{alliance_color}_activation_rp"].append(
                        score_breakdown['rp_breakdown']['activation'])

                    for robot_num, auto_mobility in enumerate(score_breakdown["auto"]["mobility"]):
                        data_dict[f"{alliance_color}_{robot_num+1}_auto_mobility"].append(
                            {"Yes": 3, "No": 0}[auto_mobility])
                    for robot_num, endgame_park in enumerate(score_breakdown["endgame"]["park_type"]):
                        data_dict[f"{alliance_color}_{robot_num+1}_endgame_park"].append(
                            endgame_park)

                    for piece_placement in ["low", "mid", "high"]:
                        for opmode in ['auto', 'scoring']:
                            opmode_in = {'auto': 'auto',
                                         'scoring': 'teleop'}[opmode]
                            data_dict[f"{alliance_color}_piece_{piece_placement}_{opmode_in}"].append(
                                score_breakdown[opmode]["pieces"][piece_placement])
                    data_dict[f"{alliance_color}_links_scored"].append(
                        score_breakdown["scoring"]["links"])

        df = pd.DataFrame(data=data_dict)
        return df

    def get_match_team_data_breakdown(self, match_data, alliance_color):
        return [
            match_data[f'{alliance_color}_points_scored'],
            match_data[f'{alliance_color}_links_scored'],
            match_data[f'{alliance_color}_piece_low_auto'],
            match_data[f'{alliance_color}_piece_mid_auto'],
            match_data[f'{alliance_color}_piece_high_auto'],
            match_data[f'{alliance_color}_piece_low_teleop'],
            match_data[f'{alliance_color}_piece_mid_teleop'],
            match_data[f'{alliance_color}_piece_high_teleop'],
        ]

    def normalize_opr(self, i):
        # helper functionto normalize OPRs to point values
        team_component_opr_normalized = i.copy(deep=True)
        team_component_opr_normalized['links_scored'] *= 5
        team_component_opr_normalized['piece_low_auto'] *= 3
        team_component_opr_normalized['piece_mid_auto'] *= 4
        team_component_opr_normalized['piece_high_auto'] *= 6
        team_component_opr_normalized['piece_low_teleop'] *= 2
        team_component_opr_normalized['piece_mid_teleop'] *= 3
        team_component_opr_normalized['piece_high_teleop'] *= 5
        return team_component_opr_normalized

    def load_data_event(self, event, data_root="data"):
        # load saved data (make sure to download w/ downloadData.py)
        with open(f"{data_root}/{event}.json", 'r') as f:
            json_data = json.load(f)

        matches = json_data['matches']
        unplayed_matches = json_data['unplayed_matches']
        oprs = json_data['oprs']
        teams = json_data['teams']

        all_match_data = self.flatten_data_matches(matches)
        qualification_matches = all_match_data.loc[all_match_data['match_type'] == 'qm']

        all_unplayed_matches = self.flatten_data_matches(
            unplayed_matches, played=False)
        qualification_matches_unplayed = all_unplayed_matches.loc[
            all_unplayed_matches['match_type'] == 'qm']

        # get team scores into a dataframe
        team_scores = []
        for _, match in qualification_matches.iterrows():
            for i, team in enumerate(match['blue_keys']):
                team_scores.append(
                    [team] + self.get_match_team_data_breakdown(match, 'blue') +
                    [match[f'blue_{i+1}_auto_mobility']] +
                    [match[f'blue_{i+1}_endgame_park']] +
                    [match['match_number']]
                )
            for i, team in enumerate(match['red_keys']):
                team_scores.append(
                    [team] + self.get_match_team_data_breakdown(match, 'red') +
                    [match[f'red_{i+1}_auto_mobility']] +
                    [match[f'red_{i+1}_endgame_park']] +
                    [match['match_number']]
                )
        team_scores = pd.DataFrame(team_scores, columns=['team_key', 'team_score', 'links_scored',
                                                         'piece_low_auto', 'piece_mid_auto', 'piece_high_auto', 'piece_low_teleop', 'piece_mid_teleop', 'piece_high_teleop',
                                                         'auto_mobility', 'endgame_park', 'match_number'])
        team_scores = team_scores.sort_values(by=['team_key'])

        # get generic team data into a dataframe
        team_data = []
        for team in teams:
            team_data.append([
                team,
                oprs.get(team, 0),
                np.mean(get_feature(team, team_scores, 'team_score')),
                np.mean(get_feature(team, team_scores, 'piece_low_auto')),
                np.mean(get_feature(team, team_scores, 'piece_mid_auto')),
                np.mean(get_feature(team, team_scores, 'piece_high_auto')),
                np.mean(get_feature(team, team_scores, 'piece_low_teleop')),
                np.mean(get_feature(team, team_scores, 'piece_mid_teleop')),
                np.mean(get_feature(team, team_scores, 'piece_high_teleop')),
                np.mean(get_feature(team, team_scores, 'links_scored')),
                np.std(get_feature(team, team_scores, 'links_scored')),
                np.mean(get_feature(team, team_scores, 'auto_mobility')),
                np.std(get_feature(team, team_scores, 'auto_mobility')),
                np.mean(get_feature(team, team_scores, 'endgame_park')),
                np.std(get_feature(team, team_scores, 'endgame_park')),
            ])
        team_data = pd.DataFrame(team_data, columns=['team_key', 'opr', 'mean_score', 'mean_piece_low_auto', 'mean_piece_mid_auto', 'mean_piece_high_auto', 'mean_piece_low_teleop', 'mean_piece_mid_teleop', 'mean_piece_high_teleop',
                                                     'mean_links_scored', 'mean_links_scored_std', 'mean_auto_mobility', 'mean_auto_mobility_std', 'mean_endgame_park', 'mean_endgame_park_std'])
        team_data.sort_values(by=['mean_score'])


        # get component opr into a dataframe
        team_component_opr_data = []
        for i, team in enumerate(teams):
            adding = [
                team, team_scores.loc[team_scores['team_key'] == team].shape[0]]
            for feature in self.opr_features:
                opr_prediction, std = stat_utils.residual_team(
                    team, qualification_matches, teams, feature)
                adding += [opr_prediction, std]
            adding += [
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_links_scored'],
                team_data.loc[team_data['team_key'] ==
                              team].iloc[0]['mean_links_scored_std'],
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_auto_mobility'],
                team_data.loc[team_data['team_key'] ==
                              team].iloc[0]['mean_auto_mobility_std'],
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_endgame_park'],
                team_data.loc[team_data['team_key'] ==
                              team].iloc[0]['mean_endgame_park_std'],
                team_data.loc[team_data['team_key']
                              == team].iloc[0]['mean_score']
            ]

            team_component_opr_data.append(adding)

        column_names = ['team_key', 'matches_played']
        for i in self.opr_features:
            column_names += [f'{i}', f'{i}_std']
        column_names += ['mean_links_scored', 'mean_links_scored_std', 'mean_auto_mobility',
                         'mean_auto_mobility_std', 'mean_endgame_park', 'mean_endgame_park_std', 'mean_score']

        team_component_opr_data = pd.DataFrame(
            team_component_opr_data, columns=column_names)
        team_component_opr_data.sort_values(by='points_scored')

        return qualification_matches, qualification_matches_unplayed, team_scores, team_data, team_component_opr_data


class PerTeamDataLoader:
    # usage example:
    # importlib.reload(src.data_loader)
    # ld = src.data_loader.PerTeamDataLoader("data")

    # qms, oprs = ld.load_filtered_event_data("ncjoh", 30)
    # oprs
    
    def __init__(self, data_folder):
        self.qm = pd.read_csv(f'{data_folder}/cache/qualification-matches.csv', converters={"red_keys":ast.literal_eval, "blue_keys":ast.literal_eval})
        self.opr_features = ['points_scored', 'piece_low_auto', 'piece_mid_auto',
                        'piece_high_auto', 'piece_low_teleop', 'piece_mid_teleop', 'piece_high_teleop']


    def get_team_matches(self, team_key=None, events=None, played_before=None):
        # get all matches (rows) where a team played
        # filter matches to only include those from events (if provided) and played before some mathc # (if provided)
        if team_key is None and events is None and played_before is None:
            raise Exception("yabe")
        
        matches_played = self.qm

        if team_key is not None:
            matches_played = self.qm.loc[
                (team_key == self.qm["blue_1_key"]) |
                (team_key == self.qm["blue_2_key"]) |
                (team_key == self.qm["blue_3_key"]) |
                (team_key == self.qm["red_1_key"]) |
                (team_key == self.qm["red_2_key"]) |
                (team_key == self.qm["red_3_key"])
            ]

        if events is not None:
            filtered = [matches_played[matches_played["match_key"].str.contains(
                event)] for event in events]
            matches_played = pd.concat(filtered).drop_duplicates(subset=["match_key"])

        if played_before is not None:
            matches_played = matches_played.loc[matches_played["match_number"]
                                                <= played_before]

        return matches_played.reset_index(drop=True)
    
    def get_mean_std_team_feature(self, team_key, matches_observing, feature, key_specific=False):
        # get the mean and std vals for some feature of a team's performance in matches_observing
        vals = []
        for _, row in matches_observing.iterrows():
            if team_key in row["red_keys"]:
                if not key_specific:
                    vals.append(row[f"red_{feature}"])
                    continue
                for i, tk in enumerate(row["red_keys"]):
                    if tk == team_key:
                        vals.append(row[f"red_{i+1}_{feature}"])
                        break
            if team_key in row["blue_keys"]:
                if not key_specific:
                    vals.append(row[f"blue_{feature}"])
                    continue
                for i, tk in enumerate(row["blue_keys"]):
                    if tk == team_key:
                        vals.append(row[f"blue_{i+1}_{feature}"])
                        break
        return np.mean(vals), np.std(vals, ddof=0)

    def calculate_teams_oprs_from_matches(self, team_keys, matches_observing):
        team_component_opr_data = []
        for i, team in enumerate(team_keys):
            adding = [team] 
            for feature in self.opr_features:
                opr_prediction, std = stat_utils.residual_team(
                    team, matches_observing, team_keys, feature)
                adding += [opr_prediction, std]
            links_scored = self.get_mean_std_team_feature(team, matches_observing, "links_scored")
            auto_mobility = self.get_mean_std_team_feature(team, matches_observing, "auto_mobility", True)
            endgame_park = self.get_mean_std_team_feature(team, matches_observing, "endgame_park", True)
            score = self.get_mean_std_team_feature(team, matches_observing, "points_scored")
            adding += [
                links_scored[0], links_scored[1],
                auto_mobility[0], auto_mobility[1],
                endgame_park[0], endgame_park[1],
                score[0], score[1]
            ]

            team_component_opr_data.append(adding)

        column_names = ['team_key']
        for i in self.opr_features:
            column_names += [f'{i}', f'{i}_std']
        column_names += ['mean_links_scored', 'mean_links_scored_std', 'mean_auto_mobility',
                         'mean_auto_mobility_std', 'mean_endgame_park', 'mean_endgame_park_std', 'mean_score', "mean_score_std"]

        team_component_opr_data = pd.DataFrame(
            team_component_opr_data, columns=column_names)
        team_component_opr_data.sort_values(by='points_scored')
        team_component_opr_data.reset_index(drop=True)
        return team_component_opr_data
    
    def load_filtered_event_data(self, event, played_before=None):
        qms = self.get_team_matches(events=[event], played_before=played_before)
        teams_looking_at = set()
        for _, match in qms.iterrows():
            teams_in_match = match["red_keys"] + match["blue_keys"]
            teams_looking_at |= set(teams_in_match)
        oprs = self.calculate_teams_oprs_from_matches(list(teams_looking_at), qms)
        return qms.fillna(0), oprs.fillna(0) # TODO fillna is probably sus
