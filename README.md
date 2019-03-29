# Sakurajima-Scouting

This is intended to be a basic program which will pull scouting data from [TBA's API](https://www.thebluealliance.com/apidocs/v3) and provide simple to understand graphs for people to use.

The things that will probably be taken into consideration are (at least) OPR, Win/Loss ratio, Ranking, and Score

The wrapper that Sakurajima will use is [1418's wrapper](https://github.com/frc1418/tbapy) (installable using `pip install tbapy --user`).

Thanks to [FRC Programming Done Right](https://frc-pdr.readthedocs.io/en/latest/analysis/basics_of_analysis.html) for inspiration and some code.

## Workflow/graphs created

### Per team

- Boxplot of score distribution
- Plot of scores over matches with best fit (gauge improvement)
- Histogram of score distribution with normal curve
- Mean and standard deviation of scores
- OPR from TBA
- Climb rate
- Qualitative scouting data
- Percentile of average team scores

### Overall

- Box plots of all team score distributions
- Mean and standard deviation of scores
- Average OPR
- List of teams ranked by score