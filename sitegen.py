import configuration
import graphing
import sys
from siteGenerator import SiteGenerator

# site generation program

# get the flags from data pasesd in 
generateImages = True

if 'help' in sys.argv:
    print("Usage: `python sitegen.pyARGUMENTS`")
    print("ARGUMENTS")
    print("help: list arguments")
    print("noimg: don't generate new images")
if 'noimg' in sys.argv:
    generateImages = False

eventId = configuration.defaultevent

# generate graphs as needed
grapher = graphing.EventGrapher(event=eventId, year=configuration.year)
if generateImages:
    grapher.graphAllTeams("docs/{}".format(configuration.imageFolder))

# generate site
siteGenerator = SiteGenerator(event=eventId, year=configuration.year)
siteGenerator.generateSite()