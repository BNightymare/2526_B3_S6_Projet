# 2526_B3_S6_Projet
# 🤖 Projet Robot Suiveur de ligne

![KiCad](https://img.shields.io/badge/Design-KiCad-blue?style=for-the-badge&logo=kicad)
![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry_Pi-red?style=for-the-badge&logo=raspberry-pi)
![Python](https://img.shields.io/badge/Code-Python-yellow?style=for-the-badge&logo=python)

---
# 20/01 - Initialisation
## Cahier des charges
Prise en main du projet pour définir les fonctionnalités du robot et les tâches à réaliser.
Voici les principaux composants du robot:
| Composant | Rôle | Datasheet |
| :--- | :--- | :--- |
| Raspberry Pi 0 2W | Cerveau du robot. C'est lui qui donne les ordres aux composants via Python | [Datasheet Raspberry Pi 0 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) |
| LMS6DSOX | Gyroscope et accéléromètre | [Datasheet LMS6DSOX](https://github.com/user-attachments/files/24759821/Datasheet.LSM6DSOX.pdf) |
| TMC2225 | Contrôle les moteurs pas à pas qui servent de roues au robot. | [Datasheet TMC2225](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC2225_datasheet_rev1.14.pdf) |
| MCP3208 | Interface entre les capteurs analogique et la Raspberry Pi. Permet de mesurer la distance des obstacles via les capteurs infrarouges sur les 8 canneaux. | [Datasheet MCP3208](https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf) |

## Github, diagramme de Gantt et attribution des tâches
**Github**
Création du dépot Github et mise en place de l'arborescence du projet.

**Diagramme de Gantt:**
Création d'un diagramme de Gant pour visualiser les étapes de conceptions du projet ainsi que la programmation dans le temps.

**Répartition des tâches:**
Le groupe s'est répartie l'étude des trois composants. Pour chaque composant, nous avons analysé la datasheet afin d'extraire les caractéristiques électriques (tensions, courants, pin...) nécessaire à la conception du schéma Kicad.

- Datasheet
- Début schéma KiCad 

---
# 21/01 - [1. PCB](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB) : Schéma Kicad 
- Clara : [Schéma du LMS6DSOX](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20LSM6DSOX)
- Lucie : [Schéma du TMC2225](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%20S6) -> [Correction TMC2225](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20TMC2225)
- Samir : [Schéma du MCP3208](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet6) -> [Correction MCP3208](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20MCP3208)

**Correction des schémas KiCad par Mr. Fiack:**
- Raspberry à besoin d'une tension de 5V;
- Pour le TMC éviter de faire un copié-collé du schéma mais plutôt dupliquer la page, ce qui permet quand on fait les modifications sur une page de les voir sur la page dupliquer;
- Eviter les labels globaux et mettre des labels hiérarchique;
- Faire attention à ne pas relier un 3.3V du MOSFET à un 3.3V de la Raspberry, cela peut créer un court-circuit;
- Faire une page dans le schéma Kicad juste pour le Power_supply;
- Mettre des LEDS dans le schéma pour vérifier que le courant passe bien;
- Brancher une résistance aux LEDS pour éviter des les faire cramer.



Clara : [Schéma complet KiCad](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB/Projet%206%20KICAD%20CLS%20COMPLET)

---
# 23/01-26/01 - [1. PCB](https://github.com/BNightymare/2526_B3_S6_Projet/tree/1.-PCB) : Routage Kicad
- Clara : Routage du PCB Complet
- Lucie : Mise à jour de la documentation
- Samir et Lucie : Recherche des composants et attribution des MPN.

# 17/02 - [1. PCB]
-Samir et Lucie : soudure du pcb.
