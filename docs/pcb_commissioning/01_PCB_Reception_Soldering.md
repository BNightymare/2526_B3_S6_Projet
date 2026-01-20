# Réception et Soudure du PCB / PCB Reception and Soldering

## 1. Réception du PCB / PCB Reception

### 1.1 Inspection visuelle initiale / Initial Visual Inspection

Avant de commencer le travail sur le PCB, effectuer une inspection visuelle complète :
Before starting work on the PCB, perform a complete visual inspection:

#### Vérifications à effectuer / Checks to Perform:

- [ ] **Intégrité du PCB** / **PCB Integrity**
  - Pas de fissures ou de délaminage / No cracks or delamination
  - Pas de rayures profondes / No deep scratches
  - Surface propre et sans contamination / Clean surface without contamination

- [ ] **Qualité de fabrication** / **Manufacturing Quality**
  - Trous métallisés corrects / Correct plated through-holes
  - Pistes continues sans coupures / Continuous traces without breaks
  - Sérigraphie lisible / Readable silkscreen
  - Masque de soudure uniforme / Uniform solder mask

- [ ] **Dimensions** / **Dimensions**
  - Vérifier les dimensions critiques avec un pied à coulisse / Verify critical dimensions with calipers
  - Vérifier l'alignement des trous de fixation / Verify alignment of mounting holes
  - Comparer avec les spécifications de conception / Compare with design specifications

### 1.2 Tests électriques préliminaires / Preliminary Electrical Tests

#### Test de continuité / Continuity Test
```
1. Configurer le multimètre en mode continuité (buzzer)
   Set multimeter to continuity mode (buzzer)
2. Vérifier la continuité entre :
   Verify continuity between:
   - VCC et GND (doit être ouverte/should be open)
   - Broches de connecteurs adjacentes (doivent être isolées/should be isolated)
   - Points test si disponibles (selon schéma/according to schematic)
```

#### Test d'isolation / Isolation Test
```
1. Mesurer la résistance entre VCC et GND
   Measure resistance between VCC and GND
2. Valeur attendue : > 10 MΩ
   Expected value: > 10 MΩ
3. Si R < 1 MΩ, inspecter pour court-circuits
   If R < 1 MΩ, inspect for short circuits
```

## 2. Préparation de la soudure / Soldering Preparation

### 2.1 Préparation de l'espace de travail / Workspace Preparation

- [ ] Surface de travail propre et ESD-safe / Clean and ESD-safe work surface
- [ ] Éclairage adéquat / Adequate lighting
- [ ] Ventilation appropriée / Appropriate ventilation
- [ ] Tous les outils à portée de main / All tools within reach

### 2.2 Préparation des composants / Component Preparation

#### Inventaire des composants / Component Inventory
```
Créer une liste de tous les composants nécessaires :
Create a list of all required components:

1. Résistances / Resistors
2. Condensateurs / Capacitors
3. Circuits intégrés / Integrated circuits
4. Connecteurs / Connectors
5. Composants spécifiques (IMU, MCP3208, etc.)
```

#### Organisation des composants / Component Organization
- Organiser par taille (du plus petit au plus grand) / Organize by size (smallest to largest)
- Étiqueter clairement chaque composant / Clearly label each component
- Vérifier les valeurs et références / Verify values and references

### 2.3 Ordre de soudure recommandé / Recommended Soldering Order

```
1. Résistances et condensateurs CMS (si applicable)
   SMD resistors and capacitors (if applicable)
   
2. Composants passifs traversants (résistances, condensateurs)
   Through-hole passive components (resistors, capacitors)
   
3. Diodes et LEDs
   Diodes and LEDs
   
4. Connecteurs
   Connectors
   
5. Supports de CI (ne pas souder les CI directement)
   IC sockets (do not solder ICs directly)
   
6. Composants sensibles à la chaleur en dernier
   Heat-sensitive components last
   
7. Insertion des CI dans leurs supports
   Insert ICs into their sockets
```

## 3. Procédures de soudure / Soldering Procedures

### 3.1 Paramètres de soudure / Soldering Parameters

#### Composants standards / Standard Components
- Température : 320-350°C
- Fil de soudure : 0.8mm, 60/40 Sn/Pb ou Sans plomb
- Temps de contact : 2-3 secondes max

#### Composants sensibles / Sensitive Components
- Température : 280-320°C
- Utiliser supports de CI / Use IC sockets
- Temps de contact minimal / Minimal contact time

### 3.2 Technique de soudure / Soldering Technique

```
1. Nettoyer la panne du fer / Clean the soldering tip
2. Étamer la panne / Tin the tip
3. Chauffer simultanément le pad et la broche / Heat both pad and pin simultaneously
4. Appliquer le fil de soudure / Apply solder wire
5. Retirer d'abord le fil, puis le fer / Remove wire first, then iron
6. Laisser refroidir naturellement / Let cool naturally
7. Inspecter la soudure / Inspect the solder joint
```

### 3.3 Critères de qualité / Quality Criteria

#### Soudure acceptable / Acceptable Solder Joint
- ✓ Forme conique ou en volcan / Conical or volcano shape
- ✓ Surface lisse et brillante / Smooth and shiny surface
- ✓ Bon mouillage du pad et de la broche / Good wetting of pad and pin
- ✓ Quantité de soudure appropriée / Appropriate amount of solder

#### Défauts à éviter / Defects to Avoid
- ✗ Soudure froide (aspect terne, granuleux) / Cold solder (dull, grainy appearance)
- ✗ Pont de soudure entre broches / Solder bridge between pins
- ✗ Soudure insuffisante / Insufficient solder
- ✗ Soudure excessive / Excessive solder
- ✗ Composant surchauffé / Overheated component

## 4. Inspection post-soudure / Post-Soldering Inspection

### 4.1 Inspection visuelle / Visual Inspection

À l'aide d'une loupe ou microscope / Using a magnifying glass or microscope:

- [ ] Toutes les soudures sont présentes / All solder joints present
- [ ] Aucun pont de soudure / No solder bridges
- [ ] Composants correctement orientés / Components correctly oriented
- [ ] Aucun composant endommagé / No damaged components
- [ ] Pas de flux résiduel excessif / No excessive flux residue

### 4.2 Nettoyage du PCB / PCB Cleaning

```
1. Si nécessaire, nettoyer avec de l'alcool isopropylique
   If necessary, clean with isopropyl alcohol
2. Utiliser une brosse douce / Use a soft brush
3. Sécher complètement avant les tests / Dry completely before testing
```

### 4.3 Tests de continuité post-soudure / Post-Soldering Continuity Tests

```
1. Vérifier que VCC et GND sont toujours isolés
   Verify VCC and GND are still isolated
2. Tester la continuité des lignes d'alimentation
   Test power line continuity
3. Vérifier les connexions critiques selon le schéma
   Verify critical connections per schematic
```

## 5. Documentation / Documentation

### 5.1 Photos à prendre / Photos to Take

- [ ] Vue d'ensemble du PCB avant soudure / Overall PCB view before soldering
- [ ] PCB après soudure (vue d'ensemble) / PCB after soldering (overview)
- [ ] Gros plans des zones critiques / Close-ups of critical areas
- [ ] Documentation des défauts éventuels / Documentation of any defects

### 5.2 Rapport de soudure / Soldering Report

Compléter le formulaire de rapport avec :
Complete the report form with:

- Date et heure / Date and time
- Nom de l'opérateur / Operator name
- Numéro de série du PCB / PCB serial number
- Liste des composants soudés / List of soldered components
- Résultats des inspections / Inspection results
- Observations et remarques / Observations and notes
- Signature / Signature

## 6. Prochaines étapes / Next Steps

Une fois la soudure terminée et inspectée avec succès :
Once soldering is completed and successfully inspected:

1. Passer aux [tests unitaires matériels](02_Hardware_Unit_Testing.md)
   Proceed to [hardware unit testing](02_Hardware_Unit_Testing.md)
2. Conserver le rapport de soudure dans le dossier du projet
   Keep the soldering report in the project folder
3. Étiqueter le PCB avec son numéro de série
   Label the PCB with its serial number

## Annexes / Appendices

### A. Liste de contrôle de réception / Reception Checklist
Voir [Reception_Checklist.md](checklists/Reception_Checklist.md)

### B. Liste de contrôle de soudure / Soldering Checklist
Voir [Soldering_Checklist.md](checklists/Soldering_Checklist.md)

### C. Références / References
- IPC-A-610: Acceptability of Electronic Assemblies
- J-STD-001: Requirements for Soldered Electrical and Electronic Assemblies
