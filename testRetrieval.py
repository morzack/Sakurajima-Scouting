import tbapy, json

jsonFile = open('secret.json', 'r')
secretJson = json.load(jsonFile)
jsonFile.close()

tba = tbapy.TBA(secretJson.get("key"))

tbaStatus = tba.status()

print("The Blue Alliance is currently {}\n".format("offline" if tbaStatus.get('is datafeed down') else "online"))

# test out team data
teamNum = 5160
team = tba.team(teamNum)
teamkey = "frc{}".format(teamNum)
print("Team {}'s motto: {}\n".format(teamNum, team.get('motto')))

# lets get some event data
events = tba.team_events(teamNum, 2018)
print("Events that {} participated in in 2018:".format(teamNum))
for i in events:
    print("-- {}: {}".format(i.event_code, i.name))

# we'll use the first listed event from now on
event = events[0]
oprs = tba.event_oprs(event.key)
print("\nMore information about: {}".format(event.name))
print("{} took place on {}".format(event.key, event.end_date))
print("{} had an OPR of {}\n".format(teamNum, oprs.get("oprs").get("frc{}".format(teamNum))))

# match time!
matches = tba.team_matches(teamNum, event=event.key, year=2018)
# using the first match...
match = matches[0]
scoreBreakdown = match.get("score_breakdown")
alliance = "red" if teamkey in match.get("alliances").get("red").get("team_keys") else "blue"
print("in one of {}'s matches, the final score for their alliance was {} and they were on the {} alliance".format(teamNum, scoreBreakdown.get(alliance).get("totalPoints"), alliance))

# print("\nMatches played in:")
# for i in matches:
#    print("-- {}".format(i.key))

# lets get scores for all qualifier matches
qualMatchScores = {}
for i in matches:
    if i.comp_level == "qm":
        qualMatchScores[i.match_number] = i.score_breakdown.get(alliance).get("totalPoints")

print("\nMatch scores:")
for i in sorted(qualMatchScores):
    print("Alliance score in match {}: {}".format(i, qualMatchScores[i]))