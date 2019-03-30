## Welcome

This is intended to be a scouting application for the 2019 FRC game, Destination Deep Space.
It will contain rankings as well as statistics and graphs for various teams competing at FRC competitions.
Don't expect for it to have to many updates except during competitions.
Hopefully most of this will be auto generated as needed to make things easier for me.

Source code can be found [here](https://github.com/morzack/Sakurajima-Scouting).

Message me at @Valis#7360 on Discord for more information.

## How to interpret this

The OPR recorded is extremely useful to see what teams are good overall, however it doesn't really give the full picture when it comes to skill.
I'd recomend pairing the OPR data with qualitative data that determines what it is that a team specializes in.

When interpreting the score graph the easiest thing to look at is the red trendline, as that can show team performance as matches progress.
Obviously a positive slope is good, and any massive dips should be recorded and checked by looking at the OPR.

The team skill breakdown section will be extremely useful when it comes down to picking teams and seeing what they are capable of doing.
At the moment the only things that will be considered automatically are the climb level and opr.
I don't think that there are any other things that can be automatically determined by just using the TBA API yet.
Sakurajima will probably calculate the score achieved in individual categories at some point using similar math to OPR, but that's not happening yet.

## At a Glance

### Overall Competition Stats

**Median match score**: 45.5

**Mean match score**: 43.05

**SD of match scores**: 13.32

![all scores](images/allScoreHistogram.png)

### All teams with OPR and Score P Value

- [Team 2642: Pitt Pirates](#2642-pitt-pirates),&nbsp;&nbsp;&nbsp;&nbsp;20.08,&nbsp;&nbsp;&nbsp;&nbsp;0.92
- [Team 2682: Boneyard Robotics](#2682-boneyard-robotics),&nbsp;&nbsp;&nbsp;&nbsp;22.13,&nbsp;&nbsp;&nbsp;&nbsp;0.78
- [Team 3215: Apollo](#3215-apollo),&nbsp;&nbsp;&nbsp;&nbsp;0.61,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 3336: Zimanators](#3336-zimanators),&nbsp;&nbsp;&nbsp;&nbsp;18.76,&nbsp;&nbsp;&nbsp;&nbsp;0.76
- [Team 3661: RoboWolves](#3661-robowolves),&nbsp;&nbsp;&nbsp;&nbsp;7.89,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 3737: Roto-Raptors](#3737-roto-raptors),&nbsp;&nbsp;&nbsp;&nbsp;18.45,&nbsp;&nbsp;&nbsp;&nbsp;0.92
- [Team 3796: Technical Assassins](#3796-technical-assassins),&nbsp;&nbsp;&nbsp;&nbsp;5.36,&nbsp;&nbsp;&nbsp;&nbsp;0.99
- [Team 3822: Neon Jets](#3822-neon-jets),&nbsp;&nbsp;&nbsp;&nbsp;11.94,&nbsp;&nbsp;&nbsp;&nbsp;0.96
- [Team 4291: AstroBots](#4291-astrobots),&nbsp;&nbsp;&nbsp;&nbsp;15.46,&nbsp;&nbsp;&nbsp;&nbsp;0.95
- [Team 435: Robodogs](#435-robodogs),&nbsp;&nbsp;&nbsp;&nbsp;13.33,&nbsp;&nbsp;&nbsp;&nbsp;0.92
- [Team 4534: Wired Wizards](#4534-wired-wizards),&nbsp;&nbsp;&nbsp;&nbsp;27.91,&nbsp;&nbsp;&nbsp;&nbsp;0.62
- [Team 4795: EastBots](#4795-eastbots),&nbsp;&nbsp;&nbsp;&nbsp;25.19,&nbsp;&nbsp;&nbsp;&nbsp;0.65
- [Team 4816: Gadget Girls](#4816-gadget-girls),&nbsp;&nbsp;&nbsp;&nbsp;5.34,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 4829: Titanium Tigers](#4829-titanium-tigers),&nbsp;&nbsp;&nbsp;&nbsp;18.44,&nbsp;&nbsp;&nbsp;&nbsp;0.92
- [Team 5160: Chargers](#5160-chargers),&nbsp;&nbsp;&nbsp;&nbsp;13.17,&nbsp;&nbsp;&nbsp;&nbsp;0.9
- [Team 5511: Cortechs Robotics](#5511-cortechs-robotics),&nbsp;&nbsp;&nbsp;&nbsp;22.75,&nbsp;&nbsp;&nbsp;&nbsp;0.84
- [Team 5544: SWIFT Robotics](#5544-swift-robotics),&nbsp;&nbsp;&nbsp;&nbsp;25.9,&nbsp;&nbsp;&nbsp;&nbsp;0.81
- [Team 5607: Team Firewall](#5607-team-firewall),&nbsp;&nbsp;&nbsp;&nbsp;16.01,&nbsp;&nbsp;&nbsp;&nbsp;0.9
- [Team 6004: f(x) Robotics](#6004-fx-robotics),&nbsp;&nbsp;&nbsp;&nbsp;13.49,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 6214: PHEnix](#6214-phenix),&nbsp;&nbsp;&nbsp;&nbsp;18.29,&nbsp;&nbsp;&nbsp;&nbsp;0.93
- [Team 6215: Armored Eagles](#6215-armored-eagles),&nbsp;&nbsp;&nbsp;&nbsp;1.08,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 6426: Robo Gladiators](#6426-robo-gladiators),&nbsp;&nbsp;&nbsp;&nbsp;6.99,&nbsp;&nbsp;&nbsp;&nbsp;0.99
- [Team 6500: GearCats](#6500-gearcats),&nbsp;&nbsp;&nbsp;&nbsp;23.82,&nbsp;&nbsp;&nbsp;&nbsp;0.84
- [Team 6512: Coastal CATastrophe](#6512-coastal-catastrophe),&nbsp;&nbsp;&nbsp;&nbsp;5.99,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 6639: The Mechanical Minds ](#6639-the-mechanical-minds),&nbsp;&nbsp;&nbsp;&nbsp;16.09,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 6729: RobCoBots](#6729-robcobots),&nbsp;&nbsp;&nbsp;&nbsp;13.68,&nbsp;&nbsp;&nbsp;&nbsp;0.97
- [Team 7029: Scotbotics](#7029-scotbotics),&nbsp;&nbsp;&nbsp;&nbsp;13.45,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 7265: Skeleton Crew](#7265-skeleton-crew),&nbsp;&nbsp;&nbsp;&nbsp;16.64,&nbsp;&nbsp;&nbsp;&nbsp;0.94
- [Team 7270: Pender Circuit Breakers](#7270-pender-circuit-breakers),&nbsp;&nbsp;&nbsp;&nbsp;4.79,&nbsp;&nbsp;&nbsp;&nbsp;1.0
- [Team 7443: Overhills Jag-Wires](#7443-overhills-jag-wires),&nbsp;&nbsp;&nbsp;&nbsp;18.91,&nbsp;&nbsp;&nbsp;&nbsp;0.95
- [Team 7463: Incandescent Mice](#7463-incandescent-mice),&nbsp;&nbsp;&nbsp;&nbsp;11.79,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 7671: Fire Hazard](#7671-fire-hazard),&nbsp;&nbsp;&nbsp;&nbsp;22.13,&nbsp;&nbsp;&nbsp;&nbsp;0.94
- [Team 7675: Spark Guardians ](#7675-spark-guardians),&nbsp;&nbsp;&nbsp;&nbsp;11.38,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 7715: Robo-Banditos](#7715-robo-banditos),&nbsp;&nbsp;&nbsp;&nbsp;6.64,&nbsp;&nbsp;&nbsp;&nbsp;0.98
- [Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors),&nbsp;&nbsp;&nbsp;&nbsp;7.28,&nbsp;&nbsp;&nbsp;&nbsp;0.99
- [Team 7890: SeQuEnCe](#7890-sequence),&nbsp;&nbsp;&nbsp;&nbsp;15.39,&nbsp;&nbsp;&nbsp;&nbsp;0.93

### Points scored per match

![Points scored per match boxplot](images/boxplot.png)

### Team skill breakdown

team | opr | z score percentile thing | opr/zs |  low hatch | high hatch | low cargo | high cargo | average climb level
--- | --- | --- | --- | :---: | :---: | :---: | :---: | :---:
[Team 4534: Wired Wizards](#4534-wired-wizards) | 27.91 | 0.62 | 45.016129032258064 |  |  |  |  | 1.889
[Team 5544: SWIFT Robotics](#5544-swift-robotics) | 25.9 | 0.81 | 31.975308641975303 |  |  |  |  | 1.111
[Team 4795: EastBots](#4795-eastbots) | 25.19 | 0.65 | 38.753846153846155 |  |  |  |  | 2.778
[Team 6500: GearCats](#6500-gearcats) | 23.82 | 0.84 | 28.357142857142858 |  |  |  |  | 0.889
[Team 5511: Cortechs Robotics](#5511-cortechs-robotics) | 22.75 | 0.84 | 27.083333333333336 | X |  | X |  | 2.444
[Team 7671: Fire Hazard](#7671-fire-hazard) | 22.13 | 0.94 | 23.54255319148936 | X |  | X |  | 1.0
[Team 2682: Boneyard Robotics](#2682-boneyard-robotics) | 22.13 | 0.78 | 28.37179487179487 | X | X | X | X | 0.889
[Team 2642: Pitt Pirates](#2642-pitt-pirates) | 20.08 | 0.92 | 21.826086956521735 | X |  | X |  | 0.889
[Team 7443: Overhills Jag-Wires](#7443-overhills-jag-wires) | 18.91 | 0.95 | 19.905263157894737 |  |  |  |  | 0.889
[Team 3336: Zimanators](#3336-zimanators) | 18.76 | 0.76 | 24.68421052631579 |  |  |  |  | 0.889
[Team 3737: Roto-Raptors](#3737-roto-raptors) | 18.45 | 0.92 | 20.054347826086953 | X | X | X | X | 0.889
[Team 4829: Titanium Tigers](#4829-titanium-tigers) | 18.44 | 0.92 | 20.043478260869566 |  |  |  |  | 1.111
[Team 6214: PHEnix](#6214-phenix) | 18.29 | 0.93 | 19.666666666666664 |  |  |  |  | 0.778
[Team 7265: Skeleton Crew](#7265-skeleton-crew) | 16.64 | 0.94 | 17.70212765957447 |  |  |  |  | 0.778
[Team 6639: The Mechanical Minds ](#6639-the-mechanical-minds) | 16.09 | 0.98 | 16.418367346938776 |  |  |  |  | 0.889
[Team 5607: Team Firewall](#5607-team-firewall) | 16.01 | 0.9 | 17.78888888888889 |  |  |  |  | 0.778
[Team 4291: AstroBots](#4291-astrobots) | 15.46 | 0.95 | 16.273684210526316 | X |  | X |  | 0.778
[Team 7890: SeQuEnCe](#7890-sequence) | 15.39 | 0.93 | 16.548387096774192 |  |  |  |  | 1.667
[Team 6729: RobCoBots](#6729-robcobots) | 13.68 | 0.97 | 14.103092783505154 |  |  |  |  | 0.778
[Team 6004: f(x) Robotics](#6004-fx-robotics) | 13.49 | 0.98 | 13.76530612244898 |  |  |  |  | 1.333
[Team 7029: Scotbotics](#7029-scotbotics) | 13.45 | 0.98 | 13.724489795918366 | X |  | X |  | 0.667
[Team 435: Robodogs](#435-robodogs) | 13.33 | 0.92 | 14.489130434782608 | X |  | X |  | 0.556
[Team 5160: Chargers](#5160-chargers) | 13.17 | 0.9 | 14.633333333333333 | X |  | X |  | 0.778
[Team 3822: Neon Jets](#3822-neon-jets) | 11.94 | 0.96 | 12.4375 |  |  |  |  | 1.0
[Team 7463: Incandescent Mice](#7463-incandescent-mice) | 11.79 | 0.98 | 12.03061224489796 | X |  | X |  | 0.889
[Team 7675: Spark Guardians ](#7675-spark-guardians) | 11.38 | 0.98 | 11.612244897959185 |  |  |  |  | 0.778
[Team 3661: RoboWolves](#3661-robowolves) | 7.89 | 1.0 | 7.89 |  |  |  |  | 0.889
[Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors) | 7.28 | 0.99 | 7.353535353535354 |  |  |  |  | 0.444
[Team 6426: Robo Gladiators](#6426-robo-gladiators) | 6.99 | 0.99 | 7.0606060606060606 |  |  |  |  | 0.778
[Team 7715: Robo-Banditos](#7715-robo-banditos) | 6.64 | 0.98 | 6.775510204081632 |  |  |  |  | 0.667
[Team 6512: Coastal CATastrophe](#6512-coastal-catastrophe) | 5.99 | 1.0 | 5.99 |  |  |  |  | 0.556
[Team 3796: Technical Assassins](#3796-technical-assassins) | 5.36 | 0.99 | 5.414141414141414 |  |  |  |  | 0.556
[Team 4816: Gadget Girls](#4816-gadget-girls) | 5.34 | 1.0 | 5.34 |  |  |  |  | 0.667
[Team 7270: Pender Circuit Breakers](#7270-pender-circuit-breakers) | 4.79 | 1.0 | 4.79 |  |  |  |  | 0.444
[Team 6215: Armored Eagles](#6215-armored-eagles) | 1.08 | 1.0 | 1.08 |  |  |  |  | 0.444
[Team 3215: Apollo](#3215-apollo) | 0.61 | 1.0 | 0.61 |  |  |  |  | 0.444

## In depth

### 2642, Pitt Pirates

**OPR**: 20.0828

**P value**: 0.92

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.889 |

![2642 scores across all recorded matches](images/frc2642.png)

[Return to top](#at-a-glance)

---

### 2682, Boneyard Robotics

**OPR**: 22.1283

**P value**: 0.78

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.889 |

![2682 scores across all recorded matches](images/frc2682.png)

[Return to top](#at-a-glance)

---

### 3215, Apollo

**OPR**: 0.6103

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.444 |

![3215 scores across all recorded matches](images/frc3215.png)

[Return to top](#at-a-glance)

---

### 3336, Zimanators

**OPR**: 18.7595

**P value**: 0.76

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.889 |

![3336 scores across all recorded matches](images/frc3336.png)

[Return to top](#at-a-glance)

---

### 3661, RoboWolves

**OPR**: 7.8851

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.889 |

![3661 scores across all recorded matches](images/frc3661.png)

[Return to top](#at-a-glance)

---

### 3737, Roto-Raptors

**OPR**: 18.4505

**P value**: 0.92

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.889 |

![3737 scores across all recorded matches](images/frc3737.png)

[Return to top](#at-a-glance)

---

### 3796, Technical Assassins

**OPR**: 5.3619

**P value**: 0.99

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.556 |

![3796 scores across all recorded matches](images/frc3796.png)

[Return to top](#at-a-glance)

---

### 3822, Neon Jets

**OPR**: 11.9404

**P value**: 0.96

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![3822 scores across all recorded matches](images/frc3822.png)

[Return to top](#at-a-glance)

---

### 4291, AstroBots

**OPR**: 15.4602

**P value**: 0.95

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.778 |

![4291 scores across all recorded matches](images/frc4291.png)

[Return to top](#at-a-glance)

---

### 435, Robodogs

**OPR**: 13.3309

**P value**: 0.92

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.556 |

![435 scores across all recorded matches](images/frc435.png)

[Return to top](#at-a-glance)

---

### 4534, Wired Wizards

**OPR**: 27.9147

**P value**: 0.62

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.889 |

![4534 scores across all recorded matches](images/frc4534.png)

[Return to top](#at-a-glance)

---

### 4795, EastBots

**OPR**: 25.1919

**P value**: 0.65

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 2.778 |

![4795 scores across all recorded matches](images/frc4795.png)

[Return to top](#at-a-glance)

---

### 4816, Gadget Girls

**OPR**: 5.343

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.667 |

![4816 scores across all recorded matches](images/frc4816.png)

[Return to top](#at-a-glance)

---

### 4829, Titanium Tigers

**OPR**: 18.4445

**P value**: 0.92

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.111 |

![4829 scores across all recorded matches](images/frc4829.png)

[Return to top](#at-a-glance)

---

### 5160, Chargers

**OPR**: 13.1708

**P value**: 0.9

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.778 |

![5160 scores across all recorded matches](images/frc5160.png)

[Return to top](#at-a-glance)

---

### 5511, Cortechs Robotics

**OPR**: 22.7546

**P value**: 0.84

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 2.444 |

![5511 scores across all recorded matches](images/frc5511.png)

[Return to top](#at-a-glance)

---

### 5544, SWIFT Robotics

**OPR**: 25.9044

**P value**: 0.81

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.111 |

![5544 scores across all recorded matches](images/frc5544.png)

[Return to top](#at-a-glance)

---

### 5607, Team Firewall

**OPR**: 16.0105

**P value**: 0.9

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![5607 scores across all recorded matches](images/frc5607.png)

[Return to top](#at-a-glance)

---

### 6004, f(x) Robotics

**OPR**: 13.4891

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.333 |

![6004 scores across all recorded matches](images/frc6004.png)

[Return to top](#at-a-glance)

---

### 6214, PHEnix

**OPR**: 18.2865

**P value**: 0.93

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![6214 scores across all recorded matches](images/frc6214.png)

[Return to top](#at-a-glance)

---

### 6215, Armored Eagles

**OPR**: 1.0829

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.444 |

![6215 scores across all recorded matches](images/frc6215.png)

[Return to top](#at-a-glance)

---

### 6426, Robo Gladiators

**OPR**: 6.9859

**P value**: 0.99

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![6426 scores across all recorded matches](images/frc6426.png)

[Return to top](#at-a-glance)

---

### 6500, GearCats

**OPR**: 23.818

**P value**: 0.84

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.889 |

![6500 scores across all recorded matches](images/frc6500.png)

[Return to top](#at-a-glance)

---

### 6512, Coastal CATastrophe

**OPR**: 5.9898

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.556 |

![6512 scores across all recorded matches](images/frc6512.png)

[Return to top](#at-a-glance)

---

### 6639, The Mechanical Minds 

**OPR**: 16.0866

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.889 |

![6639 scores across all recorded matches](images/frc6639.png)

[Return to top](#at-a-glance)

---

### 6729, RobCoBots

**OPR**: 13.6783

**P value**: 0.97

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![6729 scores across all recorded matches](images/frc6729.png)

[Return to top](#at-a-glance)

---

### 7029, Scotbotics

**OPR**: 13.4513

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.667 |

![7029 scores across all recorded matches](images/frc7029.png)

[Return to top](#at-a-glance)

---

### 7265, Skeleton Crew

**OPR**: 16.637

**P value**: 0.94

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![7265 scores across all recorded matches](images/frc7265.png)

[Return to top](#at-a-glance)

---

### 7270, Pender Circuit Breakers

**OPR**: 4.7914

**P value**: 1.0

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.444 |

![7270 scores across all recorded matches](images/frc7270.png)

[Return to top](#at-a-glance)

---

### 7443, Overhills Jag-Wires

**OPR**: 18.9113

**P value**: 0.95

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.889 |

![7443 scores across all recorded matches](images/frc7443.png)

[Return to top](#at-a-glance)

---

### 7463, Incandescent Mice

**OPR**: 11.79

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.889 |

![7463 scores across all recorded matches](images/frc7463.png)

[Return to top](#at-a-glance)

---

### 7671, Fire Hazard

**OPR**: 22.1257

**P value**: 0.94

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.0 |

![7671 scores across all recorded matches](images/frc7671.png)

[Return to top](#at-a-glance)

---

### 7675, Spark Guardians 

**OPR**: 11.381

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.778 |

![7675 scores across all recorded matches](images/frc7675.png)

[Return to top](#at-a-glance)

---

### 7715, Robo-Banditos

**OPR**: 6.6392

**P value**: 0.98

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.667 |

![7715 scores across all recorded matches](images/frc7715.png)

[Return to top](#at-a-glance)

---

### 7739, Royal Tech Warriors

**OPR**: 7.2793

**P value**: 0.99

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.444 |

![7739 scores across all recorded matches](images/frc7739.png)

[Return to top](#at-a-glance)

---

### 7890, SeQuEnCe

**OPR**: 15.3878

**P value**: 0.93

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.667 |

![7890 scores across all recorded matches](images/frc7890.png)

[Return to top](#at-a-glance)

---