# Sakurajima-Scouting

This is intended to be a program which will pull scouting data from [TBA's API](https://www.thebluealliance.com/apidocs/v3) and provide simple to understand graphs for people to use.

It also provides match prediction models that can be run throughout an event, as well as the obvious extension of match simulation.

This is intended to be run w/ python3.9.x

The TBA wrapper that this uses is [1418's wrapper](https://github.com/frc1418/tbapy).

## usage

### sourcing data

assuming you have a tba acct + api key set up:

```bash
cd scripts
python download_data.py --tba-secret $YOUR_SECRET_HERE --year 2023 --week 1 --smart-download
```

replace `2023` and `1` with respective values

use `--help` to get more info on the cmd

### building models
