import tbapy
import numpy as np
import string
import json

import configuration
from graphing import EventGrapher

class SiteGenerator:
    def __init__(self, event=configuration.defaultevent, year=configuration.year):
        self.grapher = EventGrapher(event, year)

    def generateSite(self):
        with open(configuration.qualitativeDataFile, 'r') as qualitiativeDataFile:
            qualitiativeData = json.load(qualitiativeDataFile)
        with open("docs/index.md", 'w+') as siteFile:
            # first put the basic part of the site in place
            with open("baseSite.md", 'r') as baseSite:
                siteFile.write(baseSite.read())
            
            # calculate the best teams
            siteFile.write("\n\n## At a Glance")
            siteFile.write("\n\n### Overall Competition Stats")
            siteFile.write("\n\n**Median match score**: {}".format(round(self.grapher.scoreMedian,2)))
            siteFile.write("\n\n**Mean match score**: {}".format(round(self.grapher.scoreMean, 2)))
            siteFile.write("\n\n**SD of match scores**: {}".format(round(self.grapher.scoreDeviation, 2)))
            siteFile.write("\n\n![all scores]({}/allScoreHistogram.png)".format(configuration.imageFolder))
            siteFile.write("\n\n### All teams with OPR and Score P Value\n")
            
            stringTranslator = str.maketrans('', '', string.punctuation.replace("-", ""))

            teamOprs = []
            for teamKey in self.grapher.teamKeys:
                if teamKey in self.grapher.oprs['oprs']:
                    teamOprs.append([round(self.grapher.oprs['oprs'][teamKey], 2), "{}: {}".format(teamKey[3:], self.grapher.tba.team(teamKey, simple=True)['nickname']), teamKey, self.grapher.calculateTeamStats(teamKey)])
            for opr in teamOprs:
                siteFile.write("\n- [Team {}](#{}),&nbsp;&nbsp;&nbsp;&nbsp;{},&nbsp;&nbsp;&nbsp;&nbsp;{}".format(opr[1], opr[1].strip().lower().translate(stringTranslator).replace(" ", "-"), opr[0], opr[3]))
            
            # points scored per match boxplot
            siteFile.write("\n\n### Points scored per match")
            siteFile.write("\n\n![Points scored per match boxplot](images/boxplot.png)")

            # obtain the average climb level for each team
            climbLevels = {
                "Unknown" : -1,
                "None" : 0,
                "HabLevel1" : 1,
                "HabLevel2" : 2,
                "HabLevel3" : 3
            }
            teamClimbs = {} # stored as teamKey : [sumclimb, numMatches]
            for match in self.grapher.matches:
                for teamKey in self.grapher.teamKeys:
                    alliance = "None"
                    climbLevel = -1
                    if teamKey in match['alliances']['blue']['team_keys']:
                        alliance = "blue"
                    if teamKey in match['alliances']['red']['team_keys']:
                        alliance = "red"
                    if alliance != "None" and match['score_breakdown'] != None:
                        position = match['alliances'][alliance]['team_keys'].index(teamKey) + 1
                        climbLevel = climbLevels[match['score_breakdown'][alliance]['endgameRobot{}'.format(position)]]
                    if not teamKey in teamClimbs:
                        teamClimbs[teamKey] = [0, 0] 
                    if alliance != "None" and climbLevel != -1:
                        teamClimbs[teamKey] = [teamClimbs[teamKey][0]+climbLevel, teamClimbs[teamKey][1]+1]

            f = open('dump.txt', 'w')

            # display the skill breakdown for each team
            siteFile.write("\n\n### Team skill breakdown")
            siteFile.write("\n\nteam | opr | z score percentile thing | opr/zs |  low hatch | high hatch | low cargo | high cargo | average climb level")
            siteFile.write("\n--- | --- | --- | --- | :---: | :---: | :---: | :---: | :---:")
            zscoredict = {}
            for opr in sorted(teamOprs)[::-1]:
                teamKey = opr[2]
                teamZscore = opr[3]
                teamNum = int(teamKey[3:])
                lowHatch = "X" if teamNum in qualitiativeData['hatch']['low'] else ""
                highHatch = "X" if teamNum in qualitiativeData['hatch']['high'] else ""
                lowCargo = "X" if teamNum in qualitiativeData['cargo']['low'] else ""
                highCargo = "X" if teamNum in qualitiativeData['cargo']['high'] else ""
                climb = round(teamClimbs[teamKey][0]/teamClimbs[teamKey][1], 3) if teamClimbs[teamKey][1] > 0 else 0
                oprZs = opr[0] / teamZscore
                f.write("{} {}\n".format(opr[1], oprZs))
                siteFile.write("\n[Team {}](#{}) | {} | {} | {} | {} | {} | {} | {} | {}".format(opr[1], opr[1].strip().lower().translate(stringTranslator).replace(" ", "-"), opr[0], teamZscore, oprZs, lowHatch, highHatch, lowCargo, highCargo, climb))
                zscoredict[teamKey] = teamZscore

            # then add images and opr
            siteFile.write("\n\n## In depth")
            for teamKey in self.grapher.teamKeys:
                if teamKey in self.grapher.oprs['oprs']:
                    teamNum = int(teamKey[3:])
                    siteFile.write("\n\n### {}, {}".format(teamNum, self.grapher.tba.team(teamKey, simple=True)['nickname']))
                    siteFile.write("\n\n**OPR**: {}".format(round(self.grapher.oprs['oprs'][teamKey], 4)))
                    siteFile.write("\n\n**P value**: {}".format(zscoredict[teamKey]))
                    siteFile.write("\n\n**Team Capabilities**:")
                    siteFile.write("\n\n| low hatch | high hatch | low cargo | high cargo | average climb level |")
                    siteFile.write("\n| :---: | :---: | :---: | :---: | --- |")                    
                    lowHatch = "X" if teamNum in qualitiativeData['hatch']['low'] else ""
                    highHatch = "X" if teamNum in qualitiativeData['hatch']['high'] else ""
                    lowCargo = "X" if teamNum in qualitiativeData['cargo']['low'] else ""
                    highCargo = "X" if teamNum in qualitiativeData['cargo']['high'] else ""
                    climb = round(teamClimbs[teamKey][0]/teamClimbs[teamKey][1], 3) if teamClimbs[teamKey][1] > 0 else 0
                    siteFile.write("\n| {} | {} | {} | {} | {} |".format(lowHatch, highHatch, lowCargo, highCargo, climb))
                    siteFile.write("\n\n![{} scores across all recorded matches]({}/{}.png)".format(teamKey[3:], configuration.imageFolder, teamKey))
                    siteFile.write("\n\n[Return to top](#at-a-glance)")
                    siteFile.write("\n\n---")