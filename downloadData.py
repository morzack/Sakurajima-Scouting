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

parse_taxi = {
    'Yes': 2,
    'No': 0
}

parse_endgame = {
    'Traversal': 15,
    'High': 10,
    'Mid': 6,
    'Low': 4,
    'None': 0
}

def prune_alliance_score(score_breakdown):
    return {
        'taxis': [
            parse_taxi[score_breakdown['taxiRobot1']],
            parse_taxi[score_breakdown['taxiRobot2']],
            parse_taxi[score_breakdown['taxiRobot3']]
        ],
        'endgames': [
            parse_endgame[score_breakdown['endgameRobot1']],
            parse_endgame[score_breakdown['endgameRobot2']],
            parse_endgame[score_breakdown['endgameRobot3']]
        ],

        'cargo': {
            'lower': {
                'auto': sum([score_breakdown[f"autoCargoLower{i}"] for i in ["Near", "Far", "Blue", "Red"]]),
                'teleop': sum([score_breakdown[f"teleopCargoLower{i}"] for i in ["Near", "Far", "Blue", "Red"]])
            },
            'upper': {
                'auto': sum([score_breakdown[f"autoCargoUpper{i}"] for i in ["Near", "Far", "Blue", "Red"]]),
                'teleop': sum([score_breakdown[f"teleopCargoUpper{i}"] for i in ["Near", "Far", "Blue", "Red"]])
            }
        },

        'rp_breakdown': {
            'cargo_achieved': score_breakdown['cargoBonusRankingPoint'],
            'hangar_achieved': score_breakdown['hangarBonusRankingPoint']
        },
        'rp': score_breakdown['rp'],

        'foul_count': score_breakdown['foulCount'],
        'points_scored': score_breakdown['totalPoints'] - score_breakdown['foulPoints']
    }

def download_event_data(event, output_folder="data/", week_filter=None):
    event_data = tba_client.event(event)
    if event_data["week"] is None and week_filter is not None:
        return False
    event_week = event_data["week"] + 1
    if week_filter is not None and week_filter != event_week:
        return False
    
    event_oprs = tba_client.event_oprs(event)
    event_teams = tba_client.event_teams(event, keys=True)
    event_matches = tba_client.event_matches(event)

    matches = {}
    unplayed_matches = {}
    for match in event_matches:
        if match['actual_time'] != None:
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
        else:
            unplayed_matches[match['key']] = {
                'key': match['key'],
                'match_type': match['comp_level'],
                'number': match['match_number'],

                'alliances': {
                    'red': {
                        'team_keys': match['alliances']['red']['team_keys'],
                    },
                    'blue': {
                        'team_keys': match['alliances']['blue']['team_keys'],
                    }
                },
            }

    # save the data for later use
    with open(f'{output_folder}/{event}.json', 'w') as f:
        json.dump({
            'matches': matches,
            'unplayed_matches': unplayed_matches,
            'oprs': event_oprs['oprs'] if 'oprs' in event_oprs else {},
            'teams': event_teams
        }, f)

def main():
    if sys.argv[1] == "--list-events":
        events = tba_client.events(int(sys.argv[2]), keys=True)
        print(" ".join(events))
        return
    
    if sys.argv[1] == "--smart-download":
        year = int(sys.argv[2])
        week = None
        save_dir = "data/"
        if len(sys.argv) > 3:
            week = int(sys.argv[3])
        if len(sys.argv) > 4:
            save_dir = sys.argv[4]
        events = tba_client.events(int(sys.argv[2]), keys=True)
        for event in events:
            download_event_data(event, save_dir, week)
        
        return
    
    if sys.argv[1] == "--help":
        print("downloadData.py")
        print("--list-events [year]")
        print("\tget all events in a given year")
        print("--smart-download [year] [week] [dir]")
        print("\tdownload all events from a given year (and optional week)")
        print("\tthese will automatically be placed in data/, unless dir is specified")
        print("downloadData.py [event] [event2] [event3]")
        print("\tdownload data for given events into data/")
        return

    # download data
    events = sys.argv[1:]
    for event in events:
        download_event_data(event)

if __name__ == "__main__":
    main()