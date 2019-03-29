## Welcome

This is intended to be a scouting application for the 2019 FRC game, Destination Deep Space.
It will contain rankings as well as statistics and graphs for various teams competing at FRC competitions.
Don't expect for it to have to many updates except during competitions.
Hopefully most of this will be auto generated as needed to make things easier for me.

Source code can be found [here](https://github.com/morzack/Sakurajima-Scouting).

Message me at @Valis#7360 on Discord for more information.

## How to interpret this

The OPR recoreded is extremely useful to see what teams are good overall, however it doesn't really give the full picture when it comes to skill.
I'd reccomend pairing the OPR data with qualitative data that determines what it is that a team specializes in.

When interpreting the score graph the easiest thing to look at is the red trendline, as that can show team performance as matches progress.
Obviously a positive slope is good, and any massive dips should be recorded and checked by looking at the OPR.

The team skill breakdown section will be extremely useful when it comes down to picking teams and seeing what they are capable of doing.
At the moment the only things that will be considered automatically are the climb level and opr.
I don't think that there are any other things that can be automatically determined by just using the TBA API yet.
Sakurajima will probably calculate the score achieved in individual categories at some point using similar math to OPR, but that's not happening yet.

## At a Glance

### Overall Competition Stats

**Median match score**: 33.0

**Mean match score**: 33.43

**SD of match scores**: 14.8

![all scores](images/allScoreHistogram.png)

### All teams with OPR and Score P Value

- [Team 2059: The Hitchhikers](#2059-the-hitchhikers),&nbsp;&nbsp;&nbsp;&nbsp;16.32,&nbsp;&nbsp;&nbsp;&nbsp;0.18
- [Team 2642: Pitt Pirates](#2642-pitt-pirates),&nbsp;&nbsp;&nbsp;&nbsp;19.53,&nbsp;&nbsp;&nbsp;&nbsp;0.08
- [Team 2682: Boneyard Robotics](#2682-boneyard-robotics),&nbsp;&nbsp;&nbsp;&nbsp;15.03,&nbsp;&nbsp;&nbsp;&nbsp;0.24
- [Team 3229: Hawktimus Prime](#3229-hawktimus-prime),&nbsp;&nbsp;&nbsp;&nbsp;21.83,&nbsp;&nbsp;&nbsp;&nbsp;0.04
- [Team 3336: Zimanators](#3336-zimanators),&nbsp;&nbsp;&nbsp;&nbsp;10.31,&nbsp;&nbsp;&nbsp;&nbsp;0.35
- [Team 3459: Team PyroTech](#3459-team-pyrotech),&nbsp;&nbsp;&nbsp;&nbsp;4.9,&nbsp;&nbsp;&nbsp;&nbsp;0.74
- [Team 3737: Roto-Raptors](#3737-roto-raptors),&nbsp;&nbsp;&nbsp;&nbsp;15.63,&nbsp;&nbsp;&nbsp;&nbsp;0.16
- [Team 3796: Technical Assassins](#3796-technical-assassins),&nbsp;&nbsp;&nbsp;&nbsp;7.0,&nbsp;&nbsp;&nbsp;&nbsp;0.62
- [Team 4291: AstroBots](#4291-astrobots),&nbsp;&nbsp;&nbsp;&nbsp;10.82,&nbsp;&nbsp;&nbsp;&nbsp;0.36
- [Team 435: Robodogs](#435-robodogs),&nbsp;&nbsp;&nbsp;&nbsp;8.77,&nbsp;&nbsp;&nbsp;&nbsp;0.4
- [Team 4561: TerrorBytes](#4561-terrorbytes),&nbsp;&nbsp;&nbsp;&nbsp;24.34,&nbsp;&nbsp;&nbsp;&nbsp;0.03
- [Team 4816: Gadget Girls](#4816-gadget-girls),&nbsp;&nbsp;&nbsp;&nbsp;3.47,&nbsp;&nbsp;&nbsp;&nbsp;0.62
- [Team 4828: RoboEagles](#4828-roboeagles),&nbsp;&nbsp;&nbsp;&nbsp;4.85,&nbsp;&nbsp;&nbsp;&nbsp;0.47
- [Team 5160: Chargers](#5160-chargers),&nbsp;&nbsp;&nbsp;&nbsp;12.4,&nbsp;&nbsp;&nbsp;&nbsp;0.3
- [Team 5190: Green Hope Falcons](#5190-green-hope-falcons),&nbsp;&nbsp;&nbsp;&nbsp;17.75,&nbsp;&nbsp;&nbsp;&nbsp;0.12
- [Team 5511: Cortechs Robotics](#5511-cortechs-robotics),&nbsp;&nbsp;&nbsp;&nbsp;23.92,&nbsp;&nbsp;&nbsp;&nbsp;0.04
- [Team 5518: Techno Wolves](#5518-techno-wolves),&nbsp;&nbsp;&nbsp;&nbsp;7.0,&nbsp;&nbsp;&nbsp;&nbsp;0.55
- [Team 5607: Team Firewall](#5607-team-firewall),&nbsp;&nbsp;&nbsp;&nbsp;12.12,&nbsp;&nbsp;&nbsp;&nbsp;0.29
- [Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra),&nbsp;&nbsp;&nbsp;&nbsp;15.54,&nbsp;&nbsp;&nbsp;&nbsp;0.22
- [Team 5919: JoCo RoBos](#5919-joco-robos),&nbsp;&nbsp;&nbsp;&nbsp;4.49,&nbsp;&nbsp;&nbsp;&nbsp;0.64
- [Team 6215: Armored Eagles](#6215-armored-eagles),&nbsp;&nbsp;&nbsp;&nbsp;1.17,&nbsp;&nbsp;&nbsp;&nbsp;0.82
- [Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight),&nbsp;&nbsp;&nbsp;&nbsp;-0.67,&nbsp;&nbsp;&nbsp;&nbsp;0.85
- [Team 6332: Bull City Botics](#6332-bull-city-botics),&nbsp;&nbsp;&nbsp;&nbsp;4.41,&nbsp;&nbsp;&nbsp;&nbsp;0.74
- [Team 6426: Robo Gladiators](#6426-robo-gladiators),&nbsp;&nbsp;&nbsp;&nbsp;15.88,&nbsp;&nbsp;&nbsp;&nbsp;0.24
- [Team 6500: GearCats](#6500-gearcats),&nbsp;&nbsp;&nbsp;&nbsp;12.51,&nbsp;&nbsp;&nbsp;&nbsp;0.36
- [Team 6502: DARC SIDE](#6502-darc-side),&nbsp;&nbsp;&nbsp;&nbsp;6.71,&nbsp;&nbsp;&nbsp;&nbsp;0.6
- [Team 6565: Team Bobcat](#6565-team-bobcat),&nbsp;&nbsp;&nbsp;&nbsp;11.4,&nbsp;&nbsp;&nbsp;&nbsp;0.47
- [Team 6908: Infuzed](#6908-infuzed),&nbsp;&nbsp;&nbsp;&nbsp;14.23,&nbsp;&nbsp;&nbsp;&nbsp;0.21
- [Team 7029: Scotbotics](#7029-scotbotics),&nbsp;&nbsp;&nbsp;&nbsp;4.18,&nbsp;&nbsp;&nbsp;&nbsp;0.61
- [Team 7463: Incandescent Mice](#7463-incandescent-mice),&nbsp;&nbsp;&nbsp;&nbsp;8.84,&nbsp;&nbsp;&nbsp;&nbsp;0.49
- [Team 7671: Fire Hazard](#7671-fire-hazard),&nbsp;&nbsp;&nbsp;&nbsp;13.66,&nbsp;&nbsp;&nbsp;&nbsp;0.23
- [Team 7675: Spark Guardians ](#7675-spark-guardians),&nbsp;&nbsp;&nbsp;&nbsp;17.48,&nbsp;&nbsp;&nbsp;&nbsp;0.15
- [Team 7715: Robo-Banditos](#7715-robo-banditos),&nbsp;&nbsp;&nbsp;&nbsp;6.09,&nbsp;&nbsp;&nbsp;&nbsp;0.56
- [Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors),&nbsp;&nbsp;&nbsp;&nbsp;1.32,&nbsp;&nbsp;&nbsp;&nbsp;0.88
- [Team 7763: Carrborobotics](#7763-carrborobotics),&nbsp;&nbsp;&nbsp;&nbsp;13.43,&nbsp;&nbsp;&nbsp;&nbsp;0.25
- [Team 900: The Zebracorns](#900-the-zebracorns),&nbsp;&nbsp;&nbsp;&nbsp;14.47,&nbsp;&nbsp;&nbsp;&nbsp;0.11

### Points scored per match

![Points scored per match boxplot](images/boxplot.png)

### Team skill breakdown

team | opr | z score percentile thing | low hatch | high hatch | low cargo | high cargo | average climb level
--- | --- | --- | :---: | :---: | :---: | :---: | :---:
[Team 4561: TerrorBytes](#4561-terrorbytes) | 24.34 | 0.03 | X |  | X |  | 0.947
[Team 5511: Cortechs Robotics](#5511-cortechs-robotics) | 23.92 | 0.04 | X |  | X |  | 2.842
[Team 3229: Hawktimus Prime](#3229-hawktimus-prime) | 21.83 | 0.04 |  |  |  |  | 1.067
[Team 2642: Pitt Pirates](#2642-pitt-pirates) | 19.53 | 0.08 | X |  | X |  | 0.833
[Team 5190: Green Hope Falcons](#5190-green-hope-falcons) | 17.75 | 0.12 |  | X |  | X | 0.9
[Team 7675: Spark Guardians ](#7675-spark-guardians) | 17.48 | 0.15 |  |  |  |  | 0.75
[Team 2059: The Hitchhikers](#2059-the-hitchhikers) | 16.32 | 0.18 | X |  | X |  | 2.0
[Team 6426: Robo Gladiators](#6426-robo-gladiators) | 15.88 | 0.24 |  |  |  |  | 0.75
[Team 3737: Roto-Raptors](#3737-roto-raptors) | 15.63 | 0.16 | X | X | X | X | 0.941
[Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra) | 15.54 | 0.22 | X |  | X |  | 0.857
[Team 2682: Boneyard Robotics](#2682-boneyard-robotics) | 15.03 | 0.24 | X | X | X | X | 0.733
[Team 900: The Zebracorns](#900-the-zebracorns) | 14.47 | 0.11 | X | X | X | X | 1.778
[Team 6908: Infuzed](#6908-infuzed) | 14.23 | 0.21 | X |  | X |  | 0.733
[Team 7671: Fire Hazard](#7671-fire-hazard) | 13.66 | 0.23 | X |  | X |  | 0.95
[Team 7763: Carrborobotics](#7763-carrborobotics) | 13.43 | 0.25 | X |  | X |  | 0.8
[Team 6500: GearCats](#6500-gearcats) | 12.51 | 0.36 |  |  |  |  | 0.5
[Team 5160: Chargers](#5160-chargers) | 12.4 | 0.3 | X |  | X |  | 0.933
[Team 5607: Team Firewall](#5607-team-firewall) | 12.12 | 0.29 |  |  |  |  | 0.786
[Team 6565: Team Bobcat](#6565-team-bobcat) | 11.4 | 0.47 |  |  |  |  | 1.0
[Team 4291: AstroBots](#4291-astrobots) | 10.82 | 0.36 | X |  | X |  | 0.684
[Team 3336: Zimanators](#3336-zimanators) | 10.31 | 0.35 |  |  |  |  | 0.75
[Team 7463: Incandescent Mice](#7463-incandescent-mice) | 8.84 | 0.49 | X |  | X |  | 0.583
[Team 435: Robodogs](#435-robodogs) | 8.77 | 0.4 | X |  | X |  | 0.5
[Team 5518: Techno Wolves](#5518-techno-wolves) | 7.0 | 0.55 | X | X | X | X | 0.643
[Team 3796: Technical Assassins](#3796-technical-assassins) | 7.0 | 0.62 |  |  |  |  | 0.5
[Team 6502: DARC SIDE](#6502-darc-side) | 6.71 | 0.6 | X | X | X | X | 0.5
[Team 7715: Robo-Banditos](#7715-robo-banditos) | 6.09 | 0.56 |  |  |  |  | 0.417
[Team 3459: Team PyroTech](#3459-team-pyrotech) | 4.9 | 0.74 | X |  | X |  | 1.0
[Team 4828: RoboEagles](#4828-roboeagles) | 4.85 | 0.47 | X |  | X |  | 1.65
[Team 5919: JoCo RoBos](#5919-joco-robos) | 4.49 | 0.64 |  |  |  |  | 0.5
[Team 6332: Bull City Botics](#6332-bull-city-botics) | 4.41 | 0.74 | X |  | X |  | 0.611
[Team 7029: Scotbotics](#7029-scotbotics) | 4.18 | 0.61 | X |  | X |  | 0.588
[Team 4816: Gadget Girls](#4816-gadget-girls) | 3.47 | 0.62 |  |  |  |  | 0.25
[Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors) | 1.32 | 0.88 |  |  |  |  | 0.333
[Team 6215: Armored Eagles](#6215-armored-eagles) | 1.17 | 0.82 |  |  |  |  | 0.417
[Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight) | -0.67 | 0.85 |  |  |  |  | 0.417

## In depth

### 2059, The Hitchhikers

**OPR**: 16.3164

**P value**: 0.18

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 2.0 |

![2059 scores across all recorded matches](images/frc2059.png)

[Return to top](#at-a-glance)

---

### 2642, Pitt Pirates

**OPR**: 19.5304

**P value**: 0.08

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.833 |

![2642 scores across all recorded matches](images/frc2642.png)

[Return to top](#at-a-glance)

---

### 2682, Boneyard Robotics

**OPR**: 15.0315

**P value**: 0.24

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.733 |

![2682 scores across all recorded matches](images/frc2682.png)

[Return to top](#at-a-glance)

---

### 3229, Hawktimus Prime

**OPR**: 21.8299

**P value**: 0.04

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.067 |

![3229 scores across all recorded matches](images/frc3229.png)

[Return to top](#at-a-glance)

---

### 3336, Zimanators

**OPR**: 10.3106

**P value**: 0.35

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.75 |

![3336 scores across all recorded matches](images/frc3336.png)

[Return to top](#at-a-glance)

---

### 3459, Team PyroTech

**OPR**: 4.9027

**P value**: 0.74

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.0 |

![3459 scores across all recorded matches](images/frc3459.png)

[Return to top](#at-a-glance)

---

### 3737, Roto-Raptors

**OPR**: 15.6293

**P value**: 0.16

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.941 |

![3737 scores across all recorded matches](images/frc3737.png)

[Return to top](#at-a-glance)

---

### 3796, Technical Assassins

**OPR**: 7.0035

**P value**: 0.62

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.5 |

![3796 scores across all recorded matches](images/frc3796.png)

[Return to top](#at-a-glance)

---

### 4291, AstroBots

**OPR**: 10.8234

**P value**: 0.36

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.684 |

![4291 scores across all recorded matches](images/frc4291.png)

[Return to top](#at-a-glance)

---

### 435, Robodogs

**OPR**: 8.7733

**P value**: 0.4

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.5 |

![435 scores across all recorded matches](images/frc435.png)

[Return to top](#at-a-glance)

---

### 4561, TerrorBytes

**OPR**: 24.3363

**P value**: 0.03

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.947 |

![4561 scores across all recorded matches](images/frc4561.png)

[Return to top](#at-a-glance)

---

### 4816, Gadget Girls

**OPR**: 3.4712

**P value**: 0.62

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.25 |

![4816 scores across all recorded matches](images/frc4816.png)

[Return to top](#at-a-glance)

---

### 4828, RoboEagles

**OPR**: 4.8458

**P value**: 0.47

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.65 |

![4828 scores across all recorded matches](images/frc4828.png)

[Return to top](#at-a-glance)

---

### 5160, Chargers

**OPR**: 12.3988

**P value**: 0.3

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.933 |

![5160 scores across all recorded matches](images/frc5160.png)

[Return to top](#at-a-glance)

---

### 5190, Green Hope Falcons

**OPR**: 17.7544

**P value**: 0.12

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  | X |  | X | 0.9 |

![5190 scores across all recorded matches](images/frc5190.png)

[Return to top](#at-a-glance)

---

### 5511, Cortechs Robotics

**OPR**: 23.9173

**P value**: 0.04

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 2.842 |

![5511 scores across all recorded matches](images/frc5511.png)

[Return to top](#at-a-glance)

---

### 5518, Techno Wolves

**OPR**: 7.0043

**P value**: 0.55

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.643 |

![5518 scores across all recorded matches](images/frc5518.png)

[Return to top](#at-a-glance)

---

### 5607, Team Firewall

**OPR**: 12.1203

**P value**: 0.29

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.786 |

![5607 scores across all recorded matches](images/frc5607.png)

[Return to top](#at-a-glance)

---

### 5762, FranklinBots - TEAM HYDRA

**OPR**: 15.544

**P value**: 0.22

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.857 |

![5762 scores across all recorded matches](images/frc5762.png)

[Return to top](#at-a-glance)

---

### 5919, JoCo RoBos

**OPR**: 4.4862

**P value**: 0.64

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.5 |

![5919 scores across all recorded matches](images/frc5919.png)

[Return to top](#at-a-glance)

---

### 6215, Armored Eagles

**OPR**: 1.1728

**P value**: 0.82

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.417 |

![6215 scores across all recorded matches](images/frc6215.png)

[Return to top](#at-a-glance)

---

### 6240, Eagles of the Knight

**OPR**: -0.6684

**P value**: 0.85

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.417 |

![6240 scores across all recorded matches](images/frc6240.png)

[Return to top](#at-a-glance)

---

### 6332, Bull City Botics

**OPR**: 4.4137

**P value**: 0.74

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.611 |

![6332 scores across all recorded matches](images/frc6332.png)

[Return to top](#at-a-glance)

---

### 6426, Robo Gladiators

**OPR**: 15.8847

**P value**: 0.24

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.75 |

![6426 scores across all recorded matches](images/frc6426.png)

[Return to top](#at-a-glance)

---

### 6500, GearCats

**OPR**: 12.5134

**P value**: 0.36

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.5 |

![6500 scores across all recorded matches](images/frc6500.png)

[Return to top](#at-a-glance)

---

### 6502, DARC SIDE

**OPR**: 6.7101

**P value**: 0.6

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.5 |

![6502 scores across all recorded matches](images/frc6502.png)

[Return to top](#at-a-glance)

---

### 6565, Team Bobcat

**OPR**: 11.397

**P value**: 0.47

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![6565 scores across all recorded matches](images/frc6565.png)

[Return to top](#at-a-glance)

---

### 6908, Infuzed

**OPR**: 14.2329

**P value**: 0.21

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.733 |

![6908 scores across all recorded matches](images/frc6908.png)

[Return to top](#at-a-glance)

---

### 7029, Scotbotics

**OPR**: 4.1798

**P value**: 0.61

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.588 |

![7029 scores across all recorded matches](images/frc7029.png)

[Return to top](#at-a-glance)

---

### 7463, Incandescent Mice

**OPR**: 8.8441

**P value**: 0.49

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.583 |

![7463 scores across all recorded matches](images/frc7463.png)

[Return to top](#at-a-glance)

---

### 7671, Fire Hazard

**OPR**: 13.6605

**P value**: 0.23

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.95 |

![7671 scores across all recorded matches](images/frc7671.png)

[Return to top](#at-a-glance)

---

### 7675, Spark Guardians 

**OPR**: 17.4784

**P value**: 0.15

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.75 |

![7675 scores across all recorded matches](images/frc7675.png)

[Return to top](#at-a-glance)

---

### 7715, Robo-Banditos

**OPR**: 6.095

**P value**: 0.56

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.417 |

![7715 scores across all recorded matches](images/frc7715.png)

[Return to top](#at-a-glance)

---

### 7739, Royal Tech Warriors

**OPR**: 1.321

**P value**: 0.88

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.333 |

![7739 scores across all recorded matches](images/frc7739.png)

[Return to top](#at-a-glance)

---

### 7763, Carrborobotics

**OPR**: 13.4278

**P value**: 0.25

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.8 |

![7763 scores across all recorded matches](images/frc7763.png)

[Return to top](#at-a-glance)

---

### 900, The Zebracorns

**OPR**: 14.4742

**P value**: 0.11

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 1.778 |

![900 scores across all recorded matches](images/frc900.png)

[Return to top](#at-a-glance)

---