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

- [Team 2059: The Hitchhikers](#2059-the-hitchhikers), 16.1389
- [Team 2642: Pitt Pirates](#2642-pitt-pirates), 19.1709
- [Team 2682: Boneyard Robotics](#2682-boneyard-robotics), 16.1592
- [Team 3229: Hawktimus Prime](#3229-hawktimus-prime), 21.5288
- [Team 3336: Zimanators](#3336-zimanators), 9.4145
- [Team 3459: Team PyroTech](#3459-team-pyrotech), 6.5073
- [Team 3737: Roto-Raptors](#3737-roto-raptors), 15.6448
- [Team 3796: Technical Assassins](#3796-technical-assassins), 6.2984
- [Team 4291: AstroBots](#4291-astrobots), 9.6648
- [Team 435: Robodogs](#435-robodogs), 8.872
- [Team 4561: TerrorBytes](#4561-terrorbytes), 26.6025
- [Team 4816: Gadget Girls](#4816-gadget-girls), 3.279
- [Team 4828: RoboEagles](#4828-roboeagles), 4.8828
- [Team 5160: Chargers](#5160-chargers), 12.2707
- [Team 5190: Green Hope Falcons](#5190-green-hope-falcons), 18.0139
- [Team 5511: Cortechs Robotics](#5511-cortechs-robotics), 23.3712
- [Team 5518: Techno Wolves](#5518-techno-wolves), 7.4298
- [Team 5607: Team Firewall](#5607-team-firewall), 11.7779
- [Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra), 15.5317
- [Team 5919: JoCo RoBos](#5919-joco-robos), 3.446
- [Team 6215: Armored Eagles](#6215-armored-eagles), 2.6826
- [Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight), -0.7397
- [Team 6332: Bull City Botics](#6332-bull-city-botics), 6.3735
- [Team 6426: Robo Gladiators](#6426-robo-gladiators), 14.5871
- [Team 6500: GearCats](#6500-gearcats), 12.3628
- [Team 6502: DARC SIDE](#6502-darc-side), 6.2953
- [Team 6565: Team Bobcat](#6565-team-bobcat), 11.8144
- [Team 6908: Infuzed](#6908-infuzed), 16.6968
- [Team 7029: Scotbotics](#7029-scotbotics), 2.7864
- [Team 7463: Incandescent Mice](#7463-incandescent-mice), 8.4749
- [Team 7671: Fire Hazard](#7671-fire-hazard), 13.189
- [Team 7675: Spark Guardians ](#7675-spark-guardians), 16.3663
- [Team 7715: Robo-Banditos](#7715-robo-banditos), 6.393
- [Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors), 0.9501
- [Team 7763: CARRBOROBOTICS](#7763-carrborobotics), 13.0373
- [Team 900: The Zebracorns](#900-the-zebracorns), 13.4639

### Points scored per match

![Points scored per match boxplot](images/boxplot.png)

### Team skill breakdown

team | opr | low hatch | high hatch | low cargo | high cargo | average climb level
--- | --- | :---: | :---: | :---: | :---: | :---:
[Team 4561: TerrorBytes](#4561-terrorbytes) | 26.6025 | X |  | X |  | 0.909
[Team 5511: Cortechs Robotics](#5511-cortechs-robotics) | 23.3712 | X |  | X |  | 2.727
[Team 3229: Hawktimus Prime](#3229-hawktimus-prime) | 21.5288 |  |  |  |  | 1.091
[Team 2642: Pitt Pirates](#2642-pitt-pirates) | 19.1709 | X |  | X |  | 0.818
[Team 5190: Green Hope Falcons](#5190-green-hope-falcons) | 18.0139 |  | X |  | X | 0.818
[Team 6908: Infuzed](#6908-infuzed) | 16.6968 | X |  | X |  | 0.818
[Team 7675: Spark Guardians ](#7675-spark-guardians) | 16.3663 |  |  |  |  | 0.727
[Team 2682: Boneyard Robotics](#2682-boneyard-robotics) | 16.1592 | X | X | X | X | 0.727
[Team 2059: The Hitchhikers](#2059-the-hitchhikers) | 16.1389 | X |  | X |  | 1.833
[Team 3737: Roto-Raptors](#3737-roto-raptors) | 15.6448 | X | X | X | X | 0.545
[Team 5762: FranklinBots - TEAM HYDRA](#5762-franklinbots---team-hydra) | 15.5317 | X |  | X |  | 0.833
[Team 6426: Robo Gladiators](#6426-robo-gladiators) | 14.5871 |  |  |  |  | 0.727
[Team 900: The Zebracorns](#900-the-zebracorns) | 13.4639 | X | X | X | X | 1.182
[Team 7671: Fire Hazard](#7671-fire-hazard) | 13.189 | X |  | X |  | 0.909
[Team 7763: CARRBOROBOTICS](#7763-carrborobotics) | 13.0373 | X |  | X |  | 0.727
[Team 6500: GearCats](#6500-gearcats) | 12.3628 |  |  |  |  | 0.417
[Team 5160: Chargers](#5160-chargers) | 12.2707 | X |  | X |  | 0.909
[Team 6565: Team Bobcat](#6565-team-bobcat) | 11.8144 |  |  |  |  | 1.0
[Team 5607: Team Firewall](#5607-team-firewall) | 11.7779 |  |  |  |  | 0.727
[Team 4291: AstroBots](#4291-astrobots) | 9.6648 | X |  | X |  | 0.545
[Team 3336: Zimanators](#3336-zimanators) | 9.4145 |  |  |  |  | 0.727
[Team 435: Robodogs](#435-robodogs) | 8.872 | X |  | X |  | 0.545
[Team 7463: Incandescent Mice](#7463-incandescent-mice) | 8.4749 | X |  | X |  | 0.545
[Team 5518: Techno Wolves](#5518-techno-wolves) | 7.4298 | X | X | X | X | 0.727
[Team 3459: Team PyroTech](#3459-team-pyrotech) | 6.5073 | X |  | X |  | 1.0
[Team 7715: Robo-Banditos](#7715-robo-banditos) | 6.393 |  |  |  |  | 0.455
[Team 6332: Bull City Botics](#6332-bull-city-botics) | 6.3735 | X |  | X |  | 0.636
[Team 3796: Technical Assassins](#3796-technical-assassins) | 6.2984 |  |  |  |  | 0.455
[Team 6502: DARC SIDE](#6502-darc-side) | 6.2953 | X | X | X | X | 0.5
[Team 4828: RoboEagles](#4828-roboeagles) | 4.8828 | X |  | X |  | 1.545
[Team 5919: JoCo RoBos](#5919-joco-robos) | 3.446 |  |  |  |  | 0.545
[Team 4816: Gadget Girls](#4816-gadget-girls) | 3.279 |  |  |  |  | 0.25
[Team 7029: Scotbotics](#7029-scotbotics) | 2.7864 | X |  | X |  | 0.364
[Team 6215: Armored Eagles](#6215-armored-eagles) | 2.6826 |  |  |  |  | 0.455
[Team 7739: Royal Tech Warriors](#7739-royal-tech-warriors) | 0.9501 |  |  |  |  | 0.364
[Team 6240: Eagles of the Knight](#6240-eagles-of-the-knight) | -0.7397 |  |  |  |  | 0.417

## In depth

### 2059, The Hitchhikers

**OPR**: 16.1389

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.833 |

![2059 scores across all recorded matches](images/frc2059.png)

[Return to top](#at-a-glance)

### 2642, Pitt Pirates

**OPR**: 19.1709

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.818 |

![2642 scores across all recorded matches](images/frc2642.png)

[Return to top](#at-a-glance)

### 2682, Boneyard Robotics

**OPR**: 16.1592

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.727 |

![2682 scores across all recorded matches](images/frc2682.png)

[Return to top](#at-a-glance)

### 3229, Hawktimus Prime

**OPR**: 21.5288

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.091 |

![3229 scores across all recorded matches](images/frc3229.png)

[Return to top](#at-a-glance)

### 3336, Zimanators

**OPR**: 9.4145

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.727 |

![3336 scores across all recorded matches](images/frc3336.png)

[Return to top](#at-a-glance)

### 3459, Team PyroTech

**OPR**: 6.5073

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.0 |

![3459 scores across all recorded matches](images/frc3459.png)

[Return to top](#at-a-glance)

### 3737, Roto-Raptors

**OPR**: 15.6448

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.545 |

![3737 scores across all recorded matches](images/frc3737.png)

[Return to top](#at-a-glance)

### 3796, Technical Assassins

**OPR**: 6.2984

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.455 |

![3796 scores across all recorded matches](images/frc3796.png)

[Return to top](#at-a-glance)

### 4291, AstroBots

**OPR**: 9.6648

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.545 |

![4291 scores across all recorded matches](images/frc4291.png)

[Return to top](#at-a-glance)

### 435, Robodogs

**OPR**: 8.872

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.545 |

![435 scores across all recorded matches](images/frc435.png)

[Return to top](#at-a-glance)

### 4561, TerrorBytes

**OPR**: 26.6025

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.909 |

![4561 scores across all recorded matches](images/frc4561.png)

[Return to top](#at-a-glance)

### 4816, Gadget Girls

**OPR**: 3.279

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.25 |

![4816 scores across all recorded matches](images/frc4816.png)

[Return to top](#at-a-glance)

### 4828, RoboEagles

**OPR**: 4.8828

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 1.545 |

![4828 scores across all recorded matches](images/frc4828.png)

[Return to top](#at-a-glance)

### 5160, Chargers

**OPR**: 12.2707

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.909 |

![5160 scores across all recorded matches](images/frc5160.png)

[Return to top](#at-a-glance)

### 5190, Green Hope Falcons

**OPR**: 18.0139

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  | X |  | X | 0.818 |

![5190 scores across all recorded matches](images/frc5190.png)

[Return to top](#at-a-glance)

### 5511, Cortechs Robotics

**OPR**: 23.3712

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 2.727 |

![5511 scores across all recorded matches](images/frc5511.png)

[Return to top](#at-a-glance)

### 5518, Techno Wolves

**OPR**: 7.4298

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.727 |

![5518 scores across all recorded matches](images/frc5518.png)

[Return to top](#at-a-glance)

### 5607, Team Firewall

**OPR**: 11.7779

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.727 |

![5607 scores across all recorded matches](images/frc5607.png)

[Return to top](#at-a-glance)

### 5762, FranklinBots - TEAM HYDRA

**OPR**: 15.5317

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.833 |

![5762 scores across all recorded matches](images/frc5762.png)

[Return to top](#at-a-glance)

### 5919, JoCo RoBos

**OPR**: 3.446

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.545 |

![5919 scores across all recorded matches](images/frc5919.png)

[Return to top](#at-a-glance)

### 6215, Armored Eagles

**OPR**: 2.6826

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.455 |

![6215 scores across all recorded matches](images/frc6215.png)

[Return to top](#at-a-glance)

### 6240, Eagles of the Knight

**OPR**: -0.7397

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.417 |

![6240 scores across all recorded matches](images/frc6240.png)

[Return to top](#at-a-glance)

### 6332, Bull City Botics

**OPR**: 6.3735

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.636 |

![6332 scores across all recorded matches](images/frc6332.png)

[Return to top](#at-a-glance)

### 6426, Robo Gladiators

**OPR**: 14.5871

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.727 |

![6426 scores across all recorded matches](images/frc6426.png)

[Return to top](#at-a-glance)

### 6500, GearCats

**OPR**: 12.3628

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.417 |

![6500 scores across all recorded matches](images/frc6500.png)

[Return to top](#at-a-glance)

### 6502, DARC SIDE

**OPR**: 6.2953

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 0.5 |

![6502 scores across all recorded matches](images/frc6502.png)

[Return to top](#at-a-glance)

### 6565, Team Bobcat

**OPR**: 11.8144

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 1.0 |

![6565 scores across all recorded matches](images/frc6565.png)

[Return to top](#at-a-glance)

### 6908, Infuzed

**OPR**: 16.6968

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.818 |

![6908 scores across all recorded matches](images/frc6908.png)

[Return to top](#at-a-glance)

### 7029, Scotbotics

**OPR**: 2.7864

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.364 |

![7029 scores across all recorded matches](images/frc7029.png)

[Return to top](#at-a-glance)

### 7463, Incandescent Mice

**OPR**: 8.4749

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.545 |

![7463 scores across all recorded matches](images/frc7463.png)

[Return to top](#at-a-glance)

### 7671, Fire Hazard

**OPR**: 13.189

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.909 |

![7671 scores across all recorded matches](images/frc7671.png)

[Return to top](#at-a-glance)

### 7675, Spark Guardians 

**OPR**: 16.3663

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.727 |

![7675 scores across all recorded matches](images/frc7675.png)

[Return to top](#at-a-glance)

### 7715, Robo-Banditos

**OPR**: 6.393

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.455 |

![7715 scores across all recorded matches](images/frc7715.png)

[Return to top](#at-a-glance)

### 7739, Royal Tech Warriors

**OPR**: 0.9501

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
|  |  |  |  | 0.364 |

![7739 scores across all recorded matches](images/frc7739.png)

[Return to top](#at-a-glance)

### 7763, CARRBOROBOTICS

**OPR**: 13.0373

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X |  | X |  | 0.727 |

![7763 scores across all recorded matches](images/frc7763.png)

[Return to top](#at-a-glance)

### 900, The Zebracorns

**OPR**: 13.4639

**Team Capabilities**:

| low hatch | high hatch | low cargo | high cargo | average climb level |
| :---: | :---: | :---: | :---: | --- |
| X | X | X | X | 1.182 |

![900 scores across all recorded matches](images/frc900.png)

[Return to top](#at-a-glance)