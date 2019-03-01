import tbapy
import numpy as np

import configuration
from graphing import EventGrapher

class SiteGenerator:
    def __init__(self, event=configuration.defaultevent, year=configuration.year):
        self.grapher = EventGrapher(event, year)

    def generateSite(self):
        with open("docs/index.md", 'w+') as siteFile:
            # first put the basic part of the site in place
            with open("baseSite.md", 'r') as baseSite:
                siteFile.write(baseSite.read())
            
            # then add images and opr
            siteFile.write("\n\n## In depth")
            for teamKey in self.grapher.teamKeys:
                siteFile.write("\n\n### {}, {}".format(teamKey[3:], self.grapher.tba.team(teamKey, simple=True)['nickname']))
                siteFile.write("\n\nOPR: {}".format(self.grapher.oprs['oprs'][teamKey]))
                siteFile.write("\n\n![{} scores across all recorded matches]({}/{}.png)".format(teamKey[3:], configuration.imageFolder, teamKey))