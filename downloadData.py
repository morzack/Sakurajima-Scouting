# download the data from TBA and save it for use
import tbapy
import json

import sys

# setup tbapy
secret_file = 'secret.json'
with open(secret_file, 'r') as f:
    secret_json = json.load(f)

key = secret_json['tba-key']

tba_client = tbapy.TBA(key)

# prune match data json to something that we care about

parse_init_line = {
    'None': 0,
    'Exited': 5
}

parse_endgame = {
    'None': 0,
    'Park': 5,
    'Hang': 25
}

def get_stage(score_breakdown):
    if score_breakdown['stage1Activated']:
        return 1
    elif score_breakdown['stage2Activated']:
        return 2
    elif score_breakdown['stage3Activated']:
        return 3
    else:
        return 0

def prune_alliance_score(score_breakdown):
    return {
        'init_lines': [
            parse_init_line[score_breakdown['initLineRobot1']],
            parse_init_line[score_breakdown['initLineRobot2']],
            parse_init_line[score_breakdown['initLineRobot3']]
        ],
        'endgames': [
            parse_endgame[score_breakdown['endgameRobot1']],
            parse_endgame[score_breakdown['endgameRobot2']],
            parse_endgame[score_breakdown['endgameRobot3']]
        ],

        'cells': {
            'bottom': {
                'auto': score_breakdown['autoCellsBottom'],
                'teleop': score_breakdown['teleopCellsBottom']
            },
            'outer': {
                'auto': score_breakdown['autoCellsOuter'],
                'teleop': score_breakdown['teleopCellsOuter']
            },
            'inner': {
                'auto': score_breakdown['autoCellsInner'],
                'teleop': score_breakdown['teleopCellsInner']
            }
        },

        'max_stage': get_stage(score_breakdown),
        
        'endgame_level': score_breakdown['endgameRungIsLevel'] == 'IsLevel',

        'rp': {
            'shield_operational': score_breakdown['shieldOperationalRankingPoint'],
            'shield_energized': score_breakdown['shieldEnergizedRankingPoint']
        },

        'foul_count': score_breakdown['foulCount'],
        'points_scored': score_breakdown['totalPoints'] - score_breakdown['foulPoints']
    }

def download_event_data(event):
    event_oprs = tba_client.event_oprs(event)
    event_teams = tba_client.event_teams(event, keys=True)
    event_matches = tba_client.event_matches(event)

    matches = {}
    for match in event_matches:
        matches[match['key']] = {
            'key': match['key'],
            'match_type': match['comp_level'],
            'number': match['match_number'],

            'alliances': {
                'red': {
                    'team_keys': match['alliances']['red']['team_keys'],
                    'score_breakdown': prune_alliance_score(match['score_breakdown']['red'])
                },
                'blue': {
                    'team_keys': match['alliances']['blue']['team_keys'],
                    'score_breakdown': prune_alliance_score(match['score_breakdown']['blue'])
                }
            },
        }

    # save the data for later use
    with open(f'data/{event}.json', 'w') as f:
        json.dump({
            'matches': matches,
            'oprs': event_oprs['oprs'],
            'teams': event_teams
        }, f)

# download data
events = sys.argv[1:]
for event in events:
    download_event_data(event)