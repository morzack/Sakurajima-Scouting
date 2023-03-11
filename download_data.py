# download the data from TBA and save it for use
import tbapy
import json
import pathlib

import time
from rich.progress import Progress

import sys
import os

import argparse


class CachedTbaClient:
    def __init__(self, tba_client: tbapy.TBA, cache_file: str):
        self._cache_filename = cache_file
        self.tba_client = tba_client

        self._cache = None

        if not os.path.exists(cache_file):
            self._init_cache()
            self._write_cache()
        else:
            self._read_cache()

    def _read_cache(self):
        with open(self._cache_filename, 'r') as f:
            self._cache = json.load(f)

    def _write_cache(self):
        with open(self._cache_filename, 'w') as f:
            json.dump(self._cache, f)

    def _init_cache(self):
        self._cache = {
            "events": {}
        }

    def event(self, event, cached=True):
        if not cached or event not in self._cache["events"]:
            event_data = self.tba_client.event(event)
            self._cache["events"][event] = event_data
            self._write_cache()
            return event_data
        else:
            return self._cache["events"][event]

class MatchParser:
    def prune_alliance_score(self, score_breakdown):
        pass

# prune match data json to something that we care about
class MatchParser2022(MatchParser):
    parse_taxi_2022 = {
        'Yes': 2,
        'No': 0
    }

    parse_endgame_2022 = {
        'Traversal': 15,
        'High': 10,
        'Mid': 6,
        'Low': 4,
        'None': 0
    }

    def prune_alliance_score(self, score_breakdown):
        return {
            'taxis': [
                self.parse_taxi_2022[score_breakdown['taxiRobot1']],
                self.parse_taxi_2022[score_breakdown['taxiRobot2']],
                self.parse_taxi_2022[score_breakdown['taxiRobot3']]
            ],
            'endgames': [
                self.parse_endgame_2022[score_breakdown['endgameRobot1']],
                self.parse_endgame_2022[score_breakdown['endgameRobot2']],
                self.parse_endgame_2022[score_breakdown['endgameRobot3']]
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


class MatchParser2023(MatchParser):
    docking_types = {
        "None": 0,
        "Park": 2,
        "Docked": 6,
        "Engaged": 10,
    }

    def prune_alliance_score(self, sb):
        return {
            "auto": {
                "mobility": [
                    sb["mobilityRobot1"],
                    sb["mobilityRobot2"],
                    sb["mobilityRobot3"],
                ],
                "pieces": {
                    "low": len([i for i in sb["autoCommunity"]["B"] if i != "None"]),
                    "mid": len([i for i in sb["autoCommunity"]["M"] if i != "None"]),
                    "high": len([i for i in sb["autoCommunity"]["T"] if i != "None"]),
                },
            },
            "endgame": {
                "park_type": [
                    self.docking_types[sb["endGameChargeStationRobot1"]],
                    self.docking_types[sb["endGameChargeStationRobot2"]],
                    self.docking_types[sb["endGameChargeStationRobot3"]],
                ],
            },
            "scoring": {
                "pieces": {
                    "low": len([i for i in sb["teleopCommunity"]["B"] if i != "None"]),
                    "mid": len([i for i in sb["teleopCommunity"]["M"] if i != "None"]),
                    "high": len([i for i in sb["teleopCommunity"]["T"] if i != "None"]),
                },
                "links": len(sb["links"]),
            },
            "rp_breakdown": {
                "sustainability": sb["sustainabilityBonusAchieved"],
                "activation": sb["activationBonusAchieved"],
            },
            "coop_bonus": sb["coopertitionCriteriaMet"],
            "rp": sb["rp"],
            "foul_count": sb["foulCount"],
            "points_scored": sb["totalPoints"] - sb["foulPoints"],
        }



def download_event_data(t: CachedTbaClient, year_parser: MatchParser, event, output_folder="data/"):
    event_oprs = t.tba_client.event_oprs(event)
    event_teams = t.tba_client.event_teams(event, keys=True)
    event_matches = t.tba_client.event_matches(event)

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
                        'score_breakdown': year_parser.prune_alliance_score(match['score_breakdown']['red'])
                    },
                    'blue': {
                        'team_keys': match['alliances']['blue']['team_keys'],
                        'score_breakdown': year_parser.prune_alliance_score(match['score_breakdown']['blue'])
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


def cute_execute(executor, prefixer, to_execute, description):
    with Progress() as progress:
        task = progress.add_task(description, total=len(to_execute))
        for executable in to_execute:
            if prefixer is not None:
                progress.console.print(prefixer(executable))
            executor(executable)
            progress.advance(task)


def cute_download_events(tba_client: CachedTbaClient, year_parser, to_download):
    # gives a nice little download progress bar :)

    # to_download is data structure like:
    # [{"path": "path", "events": ["events"...]}]

    events_flattened = []
    for struct in to_download:
        if not os.path.exists(struct["path"]):
            pathlib.Path(struct["path"]).mkdir(parents=True, exist_ok=True)
        for event in struct["events"]:
            events_flattened.append((struct["path"], event))

    cute_execute(lambda x: download_event_data(tba_client, year_parser, x[1], output_folder=x[0]),
                 lambda x: f"getting {x[1]}",
                 events_flattened,
                 "downloading event data :) ...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="data downloader for sakurajima")
    # config
    parser.add_argument("--tba-secret", help="TBA api key",
                        dest="tba_secret", required=True)
    parser.add_argument(
        "--year", help="year to run download script for", dest="year", required=True)
    parser.add_argument(
        "--week", help="week to run download script for", dest="week", required=False)
    parser.add_argument("--output-folder", help="output destination for downloads",
                        dest="output_folder", default="data")
    parser.add_argument("--metadata-cache", help="tba metadata cache file",
                        dest="cache_file", required=False, default=".tba_cache.json")
    parser.add_argument("--skip-metadata-caching", help="skip caching tba metadata",
                        dest="skip_cache_flag", default=False, action="store_const", const=True)

    # mode
    parser.add_argument("--list-events", help="list all events",
                        dest="list_event_flag", default=False, action="store_const", const=True)
    parser.add_argument("--smart-download", help="download all data for given year and week",
                        dest="smart_download_flag", default=False, action="store_const", const=True)
    parser.add_argument("--download-events", help="download data for a list of events",
                        dest="download_events_flag", default=False, action="store_const", const=True)

    # (if events) events to grab
    parser.add_argument(
        "events", help="events to be downloaded (for --download-events)", nargs="*")

    args, _ = parser.parse_known_args()

    if len([i for i in [
        args.list_event_flag,
        args.smart_download_flag,
        args.download_events_flag
    ] if i is True]) != 1:
        print("please select a single mode")
        sys.exit(1)

    use_cache = not args.skip_cache_flag
    cache_file = args.cache_file

    tba_secret = args.tba_secret
    _tba_client = tbapy.TBA(tba_secret)
    t = CachedTbaClient(_tba_client, cache_file)

    year = int(args.year)
    week = int(args.week) if args.week is not None else None
    output_folder = args.output_folder

    year_parser = None
    ok_years = [2022, 2023]
    if year not in ok_years:
        print(f"please use a year in {ok_years}")
        sys.exit(1)
    if year == 2022:
        year_parser = MatchParser2022()
    elif year == 2023:
        year_parser = MatchParser2023()

    if args.list_event_flag:
        events = t.tba_client.events(year, keys=True)
        print(" ".join(events))
        sys.exit(0)

    if args.smart_download_flag:
        events = t.tba_client.events(year, keys=True)

        if week != None:
            events_tmp = []

            def _filter_event(event_in):
                global events_tmp
                data = t.event(event_in, cached=use_cache)
                if data["week"] == None or data["week"]+1 != week:
                    return
                events_tmp.append(event_in)
            cute_execute(_filter_event, None, events,
                         "prechecking events :) ...")
            events = events_tmp
        cute_download_events(t, year_parser, [
            {"path": os.path.join(
                output_folder, f"week{week}"), "events": events}
        ])
        sys.exit(0)

    if args.download_events_flag:
        events = args.events
        cute_download_events(t, year_parser, [
            {"path": output_folder, "events": events}
        ])
        sys.exit(0)
