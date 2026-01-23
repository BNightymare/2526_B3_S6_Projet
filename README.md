# 2526_B3_S6_Projet
| Composant | Rôle | Datasheet |
| :--- | :--- | :--- |
| Raspberry Pi 0 2W | Cerveau du robot. C'est lui qui donne les ordres aux composants via Python | https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ |
| TMC2225 | Contrôle les moteurs pas à pas qui servent de roues au robot. | https://www.analog.com/media/en/technical-documentation/data-sheets/TMC2225_datasheet_rev1.14.pdf |
| MCP3208 | Interface entre les capteurs analogique et la Raspberry Pi. Permet de mesurer la distance des obstacles via les capteurs infrarouges sur les 8 canneaux. | https://ww1.microchip.com/downloads/en/DeviceDoc/21298E.pdf 

# **20/01 Initialisation et Cahier des charges**
## Diagramme de Gant et Attribution des tâches  
#### Cahier des charges: Prise en main du projet pour définir les fonctionnalités du robot et les tâches à réaliser;
#### Gestion de Projet: 
##### -Planning: Création d'un diagramme de Gant pour visualiser les étapes de conceptions du projet ainsi que la programmatiçon dans le temps;
##### -Github: création du dépot Github et mise en place de l'arborescence du projet.
#### Etude technique et recherche:
##### Le groupe s'est répartie l'étude des trois composants. Pour chaque composant, nous avons analysé la datasheet afin d'extraire les caractéristiques électriques ( tensions, courants, pin...) nécessaire à la conception du schéma Kicad.


# 21/01 Schéma Kicad
## Samir: Schéma du MCP3208
## Clara: Schéma du LMS6DSOX
## Lucie: Schéma du TMC2225
