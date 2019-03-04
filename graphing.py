import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tbapy
import json

import configuration

class EventGrapher:
    def __init__(self, event=configuration.defaultevent, year=configuration.year):
        jsonFile = open('secret.json', 'r')
        secretJson = json.load(jsonFile)
        jsonFile.close()

        self.tba = tbapy.TBA(secretJson.get("key"))

        self.event = "{}{}".format(year, event)
        self.year = year
        self.matches = self.tba.event_matches(self.event)
        self.teamKeys = self.tba.event_teams(self.event, keys=True)
        self.oprs = self.tba.event_oprs(self.event)
        
        plt.xkcd()

    def graphAllTeams(self, folderName):
        """
        use all graph methods to graph all teams that were at the event
            :param folderName: folder to deposit graphs into
        """
        for team in self.teamKeys:
            self.graphTeamScores(team, "{}/{}.png".format(folderName, team))
            print("Saved {}/{}.png".format(folderName, team))

    def teamBoxPlot(self, filename, teamKeys):
        """
        graph side by side violin plots for the specified teams
            :param filename: the file to save the plot into
            :param teamKeys: list of keys (using the TBA standard) referring to teams to graph
        """
        matplotlib.style.use(configuration.matplotlibStyle)
        matchScores = []
        for team in teamKeys:
            scores = []
            for match in self.matches:
                tAlliance = "None"
                for alliance in ['red', 'blue']:
                    if team in match['alliances'][alliance]['team_keys']:
                        tAlliance = alliance
                        break
                if match['comp_level'] == 'qm' and tAlliance != "None" and match['alliances'][tAlliance]['score'] > 0:
                    scores.append(match['alliances'][tAlliance]['score'])
            matchScores.append(sorted(scores)[::-1])
        tempScores = sorted(zip(matchScores, teamKeys))
        scores, teamKeys = zip(*tempScores)
        plt.figure(figsize=(13, 13), dpi=80)
        plt.boxplot(scores, showmeans=False, vert=False)
        plt.gca().xaxis.grid(True)
        plt.gca().yaxis.grid(True)
        plt.gca().set_xlabel("Match Scores")
        plt.title("Distribution of Scores at {}".format(self.event))
        labels = []
        for i in teamKeys:
            labels.append("Team {}, {}".format(i[3:], self.tba.team(i, simple=True)['nickname']))
        plt.setp(plt.gca(), yticks=[y+1 for y in range(len(teamKeys))], yticklabels=labels)
        # plt.show()
        plt.savefig(filename, bbox_inches='tight')
        plt.clf()

    def graphTeamScores(self, team, filename):
        """
        generate and save a graph with match scores for a team at an event
            :param team: team to use, expects team number as an int like 5160 or 254
            :param filename: filename to save graph to
        """
        matplotlib.style.use(configuration.matplotlibStyle)
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
            if match.comp_level == "qm" and teamAlliance != "None" and match['alliances'][teamAlliance]['score'] > 0:
                qualMatchScores.append((match['match_number'], match['alliances'][teamAlliance]['score']))
        qualMatchScores.sort()
        # make a trendline
        data = np.array(qualMatchScores)
        if len(data) == 0:
            return
        x, y = data[:,0], data[:,1]
        polyfit = np.polyfit(x, y, 1)
        trend = np.poly1d(polyfit)
        # make plot
        plt.gca().set_ylim([configuration.minScore, configuration.maxScore])
        plt.plot(x, y)
        plt.plot(x, trend(x), 'r--')
        plt.title("Match scores from {} at {}".format(team, self.event))
        plt.xlabel("Match")
        plt.ylabel("Score")
        plt.savefig(filename, bbox_inches='tight')
        plt.clf()