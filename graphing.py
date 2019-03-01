import numpy as np
import matplotlib.pyplot as plt
import tbapy
import json

import configuration

class EventGrapher:
    def __init__(self, event, year=2019):
        jsonFile = open('secret.json', 'r')
        secretJson = json.load(jsonFile)
        jsonFile.close()

        self.tba = tbapy.TBA(secretJson.get("key"))

        self.event = event
        self.year = year
        self.matches = self.tba.event_matches("{}{}".format(year, event))

    def graphTeamScores(self, team, filename):
        """
        generate and save a graph with match scores for a team at an event
            :param team: team to use, expects team number as an int like 5160 or 254
            :param filename: filename to save graph to
        """
        # get the team key
        teamKey = self.tba.team_key(team)
        # first collect the data needed
        qualMatchScores = []
        for match in self.matches:
            teamAlliance = "None"
            for alliance in ["red", "blue"]:
                if teamKey in match['alliances'][alliance]['team_keys']:
                    teamAlliance = alliance
                    break
            if match.comp_level == "qm" and teamAlliance != "None":
                qualMatchScores.append((match['match_number'], match['alliances'][teamAlliance]['score']))
        qualMatchScores.sort()
        # make a trendline
        data = np.array(qualMatchScores)
        x, y = data[:,0], data[:,1]
        polyfit = np.polyfit(x, y, 1)
        trend = np.poly1d(polyfit)
        # make plot
        plt.plot(x, y)
        plt.plot(x, trend(x), 'r--')
        plt.title("Match scores from {} at {}".format(team, self.event))
        plt.xlabel("Match")
        plt.ylabel("Score")
        plt.savefig(filename, bbox_inches='tight')