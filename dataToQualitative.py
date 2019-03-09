filePath = "data.csv"

f = open(filePath, 'r')
data = f.read().split("\n")
f.close()

hatchLow = []
hatchHigh = []

cargoLow = []
cargoHigh = []


for teamData in data:
    team = teamData.split(",")
    if teamData != "":
        teamNum = team[0]
        if int(team[1]) > 0:
            hatchLow.append(teamNum)
        if int(team[2]) > 0:
            hatchHigh.append(teamNum)
        if int(team[3]) > 0:
            cargoLow.append(teamNum)
        if int(team[4]) > 0:
            cargoHigh.append(teamNum)

import json

j = {
    "hatch" : {
        "low" : hatchLow,
        "high" : hatchHigh
    },
    "cargo" : {
        "low" : hatchLow,
        "high" : hatchHigh
    }
}

print(json.dumps(j))