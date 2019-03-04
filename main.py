from graphing import EventGrapher

grapher = EventGrapher("ncth", year=2018)

grapher.graphTeamScores(5160, "5160")

grapher.teamBoxPlot("test", grapher.teamKeys)
