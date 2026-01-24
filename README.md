# 2526_B3_S6_Projet
| Composant | Rôle | Datasheet |
| :--- | :--- | :--- |
| Raspberry Pi 0 2W | Cerveau du robot. C'est lui qui donne les ordres aux composants via Python | [Datasheet Raspberry Pi 0 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) |
| LMS6DSOX | Gyroscope et accéléromètre | [Datasheet LMS6DSOX](https://github.com/user-attachments/files/24759821/Datasheet.LSM6DSOX.pdf) |
| TMC2225 | Contrôle les moteurs pas à pas qui servent de roues au robot. | [Datasheet TMC2225](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC2225_datasheet_rev1.14.pdf) |
| MCP3208 | Interface entre les capteurs analogique et la Raspberry Pi. Permet de mesurer la distance des obstacles via les capteurs infrarouges sur les 8 canneaux. | [Datasheet MCP3208](https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf) |

---
# 20/01 - Initialisation
## Cahier des charges
Prise en main du projet pour définir les fonctionnalités du robot et les tâches à réaliser

## Github, diagramme de Gantt et attribution des tâches
**Github**
Création du dépot Github et mise en place de l'arborescence du projet.

**Diagramme de Gantt**
Création d'un diagramme de Gant pour visualiser les étapes de conceptions du projet ainsi que la programmatiçon dans le temps

**Répartition des tâches**
Le groupe s'est répartie l'étude des trois composants. Pour chaque composant, nous avons analysé la datasheet afin d'extraire les caractéristiques électriques (tensions, courants, pin...) nécessaire à la conception du schéma Kicad.

- Datasheet
- Début schéma KiCad 

---
# 21/01 - [1. PCB](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB) : Schéma Kicad 
- Clara : [Schéma du LMS6DSOX](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20LSM6DSOX)
- Lucie : [Schéma du TMC2225](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%20S6) -> [Correction TMC2225](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20TMC2225)
- Samir : [Schéma du MCP3208](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet6) -> [Correction MCP3208](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20MCP3208)

Correction des schémas KiCad

Clara : [Schéma complet KiCad](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20CLS%20COMPLET)

---
# 23/01 - [1. PCB](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB) : Routage Kicad
- Clara : Routage du PCB Complet
