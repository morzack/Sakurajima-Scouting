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

### All teams with OPR

- [Team 2059: The Hitchhikers](#2059-the-hitchhikers), 9.6667
- [Team 2642: Pitt Pirates](#2642-pitt-pirates), 3.6667
- [Team 2682: Boneyard Robotics](#2682-boneyard-robotics), 15.0
- [Team 3229: Hawktimus Prime](#3229-hawktimus-prime), 15.6667
- [Team 3336: Zimanators](#3336-zimanators), 9.6667
- [Team 3459: Team PyroTech](#3459-team-pyrotech), 4.3333
- [Team 3737: Roto-Raptors](#3737-roto-raptors), 4.6667
- [Team 3796: Technical Assassins](#3796-technical-assassins), 2.0
- [Team 4291: AstroBots](#4291-astrobots), 4.0
- [Team 435: Robodogs](#435-robodogs), 1.0
- [Team 4561: TerrorBytes](#4561-terrorbytes), 9.6667
- [Team 4816: Gadget Girls](#4816-gadget-girls), 2.0
- [Team 4828: RoboEagles](#4828-roboeagles), 3.6667
- [Team 5160: Chargers](#5160-chargers), 15.6667
- [Team 5190: Green Hope Falcons](#5190-green-hope-falcons), 12.3333
- [Team 5511: Cortechs Robotics](#5511-cortechs-robotics), 6.3333
- [Team 5518: Techno Wolves](#5518-techno-wolves), 6.3333
- [Team 5607: Team Firewall](#5607-team-firewall), 12.3333
- [Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra), 16.3333
- [Team 5919: JoCo RoBos](#5919-joco-robos), 2.0
- [Team 6215: Armored Eagles](#6215-armored-eagles), 6.3333
- [Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight), 1.0
- [Team 6332: Bull City Botics](#6332-bull-city-botics), 4.0
- [Team 6426: Robo Gladiators](#6426-robo-gladiators), 4.3333
- [Team 6500: GearCats](#6500-gearcats), 4.6667
- [Team 6502: DARC SIDE](#6502-darc-side), 15.0
- [Team 6565: Team Bobcat](#6565-team-bobcat), 12.3333
- [Team 6908: Infuzed](#6908-infuzed), 15.0
- [Team 7029: Scotbotics](#7029-scotbotics), 3.6667
- [Team 7463: Incandescent Mice](#7463-incandescent-mice), 4.6667
- [Team 7671: Fire Hazard](#7671-fire-hazard), 15.6667
- [Team 7675: Spark Guardians ](#7675-spark-guardians), 16.3333
- [Team 7715: Robo-Banditos](#7715-robo-banditos), 4.3333
- [Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors), 1.0
- [Team 7763: CARRBOROBOTICS](#7763-carrborobotics), 4.0
- [Team 900: The Zebracorns](#900-the-zebracorns), 16.3333

### Points scored per match

![Points scored per match boxplot](images/boxplot.png)

### Team skill breakdown

team | opr | low hatch | low cargo | high hatch | high cargo | average climb level
--- | --- | :---: | :---: | :---: | :---: | :---:
[Team 900: The Zebracorns](#900-the-zebracorns) | 16.3333 |  |  |  |  | 3.0
[Team 7675: Spark Guardians ](#7675-spark-guardians) | 16.3333 |  |  |  |  | 0.0
[Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra) | 16.3333 |  |  |  |  | 1.0
[Team 7671: Fire Hazard](#7671-fire-hazard) | 15.6667 |  |  |  |  | 1.0
[Team 5160: Chargers](#5160-chargers) | 15.6667 | X |  | X |  | 1.0
[Team 3229: Hawktimus Prime](#3229-hawktimus-prime) | 15.6667 |  |  |  |  | 1.0
[Team 6908: Infuzed](#6908-infuzed) | 15.0 |  |  |  |  | 1.0
[Team 6502: DARC SIDE](#6502-darc-side) | 15.0 |  |  |  |  | 0.0
[Team 2682: Boneyard Robotics](#2682-boneyard-robotics) | 15.0 |  |  |  |  | 1.0
[Team 6565: Team Bobcat](#6565-team-bobcat) | 12.3333 |  |  |  |  | 1.0
[Team 5607: Team Firewall](#5607-team-firewall) | 12.3333 |  |  |  |  | 1.0
[Team 5190: Green Hope Falcons](#5190-green-hope-falcons) | 12.3333 |  |  |  |  | 1.0
[Team 4561: TerrorBytes](#4561-terrorbytes) | 9.6667 |  |  |  |  | 1.0
[Team 3336: Zimanators](#3336-zimanators) | 9.6667 |  |  |  |  | 0.0
[Team 2059: The Hitchhikers](#2059-the-hitchhikers) | 9.6667 |  |  |  |  | 1.0
[Team 6215: Armored Eagles](#6215-armored-eagles) | 6.3333 |  |  |  |  | 0.0
[Team 5518: Techno Wolves](#5518-techno-wolves) | 6.3333 |  |  |  |  | 1.0
[Team 5511: Cortechs Robotics](#5511-cortechs-robotics) | 6.3333 |  |  |  |  | 0.0
[Team 7463: Incandescent Mice](#7463-incandescent-mice) | 4.6667 |  |  |  |  | 0.0
[Team 6500: GearCats](#6500-gearcats) | 4.6667 |  |  |  |  | 0.0
[Team 3737: Roto-Raptors](#3737-roto-raptors) | 4.6667 |  |  |  |  | 1.0
[Team 7715: Robo-Banditos](#7715-robo-banditos) | 4.3333 |  |  |  |  | 0.0
[Team 6426: Robo Gladiators](#6426-robo-gladiators) | 4.3333 |  |  |  |  | 0.0
[Team 3459: Team PyroTech](#3459-team-pyrotech) | 4.3333 |  |  |  |  | 1.0
[Team 7763: CARRBOROBOTICS](#7763-carrborobotics) | 4.0 |  |  |  |  | 0.0
[Team 6332: Bull City Botics](#6332-bull-city-botics) | 4.0 |  |  |  |  | 0.0
[Team 4291: AstroBots](#4291-astrobots) | 4.0 |  |  |  |  | 0.0
[Team 7029: Scotbotics](#7029-scotbotics) | 3.6667 |  |  |  |  | 0.0
[Team 4828: RoboEagles](#4828-roboeagles) | 3.6667 |  |  |  |  | 1.0
[Team 2642: Pitt Pirates](#2642-pitt-pirates) | 3.6667 |  |  |  |  | 1.0
[Team 5919: JoCo RoBos](#5919-joco-robos) | 2.0 |  |  |  |  | 0.0
[Team 4816: Gadget Girls](#4816-gadget-girls) | 2.0 |  |  |  |  | 0.0
[Team 3796: Technical Assassins](#3796-technical-assassins) | 2.0 |  |  |  |  | 0.0
[Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors) | 1.0 |  |  |  |  | 0.0
[Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight) | 1.0 |  |  |  |  | 0.0
[Team 435: Robodogs](#435-robodogs) | 1.0 |  |  |  |  | 0.0

## In depth

### 2059, The Hitchhikers

**OPR**: 9.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![2059 scores across all recorded matches](images/frc2059.png)

[Return to top](#at-a-glance)

### 2642, Pitt Pirates

**OPR**: 3.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![2642 scores across all recorded matches](images/frc2642.png)

[Return to top](#at-a-glance)

### 2682, Boneyard Robotics

**OPR**: 15.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![2682 scores across all recorded matches](images/frc2682.png)

[Return to top](#at-a-glance)

### 3229, Hawktimus Prime

**OPR**: 15.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![3229 scores across all recorded matches](images/frc3229.png)

[Return to top](#at-a-glance)

### 3336, Zimanators

**OPR**: 9.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![3336 scores across all recorded matches](images/frc3336.png)

[Return to top](#at-a-glance)

### 3459, Team PyroTech

**OPR**: 4.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![3459 scores across all recorded matches](images/frc3459.png)

[Return to top](#at-a-glance)

### 3737, Roto-Raptors

**OPR**: 4.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![3737 scores across all recorded matches](images/frc3737.png)

[Return to top](#at-a-glance)

### 3796, Technical Assassins

**OPR**: 2.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![3796 scores across all recorded matches](images/frc3796.png)

[Return to top](#at-a-glance)

### 4291, AstroBots

**OPR**: 4.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![4291 scores across all recorded matches](images/frc4291.png)

[Return to top](#at-a-glance)

### 435, Robodogs

**OPR**: 1.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![435 scores across all recorded matches](images/frc435.png)

[Return to top](#at-a-glance)

### 4561, TerrorBytes

**OPR**: 9.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![4561 scores across all recorded matches](images/frc4561.png)

[Return to top](#at-a-glance)

### 4816, Gadget Girls

**OPR**: 2.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![4816 scores across all recorded matches](images/frc4816.png)

[Return to top](#at-a-glance)

### 4828, RoboEagles

**OPR**: 3.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![4828 scores across all recorded matches](images/frc4828.png)

[Return to top](#at-a-glance)

### 5160, Chargers

**OPR**: 15.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.0 |

![5160 scores across all recorded matches](images/frc5160.png)

[Return to top](#at-a-glance)

### 5190, Green Hope Falcons

**OPR**: 12.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![5190 scores across all recorded matches](images/frc5190.png)

[Return to top](#at-a-glance)

### 5511, Cortechs Robotics

**OPR**: 6.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![5511 scores across all recorded matches](images/frc5511.png)

[Return to top](#at-a-glance)

### 5518, Techno Wolves

**OPR**: 6.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![5518 scores across all recorded matches](images/frc5518.png)

[Return to top](#at-a-glance)

### 5607, Team Firewall

**OPR**: 12.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![5607 scores across all recorded matches](images/frc5607.png)

[Return to top](#at-a-glance)

### 5762, FranklinBots - TEAM HYDRA

**OPR**: 16.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![5762 scores across all recorded matches](images/frc5762.png)

[Return to top](#at-a-glance)

### 5919, JoCo RoBos

**OPR**: 2.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![5919 scores across all recorded matches](images/frc5919.png)

[Return to top](#at-a-glance)

### 6215, Armored Eagles

**OPR**: 6.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6215 scores across all recorded matches](images/frc6215.png)

[Return to top](#at-a-glance)

### 6240, Eagles of the Knight

**OPR**: 1.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6240 scores across all recorded matches](images/frc6240.png)

[Return to top](#at-a-glance)

### 6332, Bull City Botics

**OPR**: 4.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6332 scores across all recorded matches](images/frc6332.png)

[Return to top](#at-a-glance)

### 6426, Robo Gladiators

**OPR**: 4.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6426 scores across all recorded matches](images/frc6426.png)

[Return to top](#at-a-glance)

### 6500, GearCats

**OPR**: 4.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6500 scores across all recorded matches](images/frc6500.png)

[Return to top](#at-a-glance)

### 6502, DARC SIDE

**OPR**: 15.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![6502 scores across all recorded matches](images/frc6502.png)

[Return to top](#at-a-glance)

### 6565, Team Bobcat

**OPR**: 12.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![6565 scores across all recorded matches](images/frc6565.png)

[Return to top](#at-a-glance)

### 6908, Infuzed

**OPR**: 15.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![6908 scores across all recorded matches](images/frc6908.png)

[Return to top](#at-a-glance)

### 7029, Scotbotics

**OPR**: 3.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7029 scores across all recorded matches](images/frc7029.png)

[Return to top](#at-a-glance)

### 7463, Incandescent Mice

**OPR**: 4.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7463 scores across all recorded matches](images/frc7463.png)

[Return to top](#at-a-glance)

### 7671, Fire Hazard

**OPR**: 15.6667

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![7671 scores across all recorded matches](images/frc7671.png)

[Return to top](#at-a-glance)

### 7675, Spark Guardians 

**OPR**: 16.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7675 scores across all recorded matches](images/frc7675.png)

[Return to top](#at-a-glance)

### 7715, Robo-Banditos

**OPR**: 4.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7715 scores across all recorded matches](images/frc7715.png)

[Return to top](#at-a-glance)

### 7739, Royal Tech Warriors

**OPR**: 1.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7739 scores across all recorded matches](images/frc7739.png)

[Return to top](#at-a-glance)

### 7763, CARRBOROBOTICS

**OPR**: 4.0

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.0 |

![7763 scores across all recorded matches](images/frc7763.png)

[Return to top](#at-a-glance)

### 900, The Zebracorns

**OPR**: 16.3333

**Team Capabilities**:

| low hatch | low cargo | high hatch | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 3.0 |

![900 scores across all recorded matches](images/frc900.png)

[Return to top](#at-a-glance)