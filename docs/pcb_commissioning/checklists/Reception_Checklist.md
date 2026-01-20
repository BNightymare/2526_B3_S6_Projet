# Checklist de Réception du PCB / PCB Reception Checklist

**Date:** _______________  
**Opérateur / Operator:** _______________  
**Numéro de série PCB / PCB Serial Number:** _______________  
**Fournisseur / Supplier:** _______________  

## 1. Inspection de l'emballage / Package Inspection

- [ ] Emballage intact, pas de dommages visibles / Package intact, no visible damage
- [ ] Emballage antistatique approprié / Appropriate antistatic packaging
- [ ] Étiquetage correct / Correct labeling
- [ ] Documentation incluse / Documentation included

**Commentaires / Comments:**
_______________________________________________________

## 2. Quantité et référence / Quantity and Reference

- [ ] Quantité correcte reçue / Correct quantity received
  - Commandé / Ordered: _____
  - Reçu / Received: _____
- [ ] Références correspondent à la commande / References match order
- [ ] Numéro de lot visible / Batch number visible: _______________

## 3. Inspection visuelle du PCB / PCB Visual Inspection

### 3.1 Intégrité physique / Physical Integrity

- [ ] Pas de fissures / No cracks
- [ ] Pas de délaminage / No delamination
- [ ] Pas de rayures profondes / No deep scratches
- [ ] Bords lisses et réguliers / Smooth and regular edges
- [ ] Pas de contamination visible / No visible contamination

### 3.2 Qualité de fabrication / Manufacturing Quality

- [ ] Trous métallisés corrects / Correct plated through-holes
  - Aucun trou bouché / No blocked holes
  - Métallisation visible / Metallization visible
- [ ] Pistes continues / Continuous traces
  - Pas de coupures visibles / No visible breaks
  - Largeur uniforme / Uniform width
- [ ] Sérigraphie / Silkscreen
  - Lisible et claire / Readable and clear
  - Correctement alignée / Correctly aligned
  - Pas de bavures / No smudges
- [ ] Masque de soudure / Solder mask
  - Couleur uniforme / Uniform color
  - Bien appliqué / Well applied
  - Pas de bulles ou défauts / No bubbles or defects
- [ ] Finition des pads / Pad finish
  - Surface lisse / Smooth surface
  - Pas d'oxydation / No oxidation
  - Finition uniforme (HASL, ENIG, etc.) / Uniform finish

## 4. Vérifications dimensionnelles / Dimensional Verifications

### 4.1 Dimensions générales / Overall Dimensions

- [ ] Longueur / Length: _____ mm (spec: _____ mm ± _____ mm)
- [ ] Largeur / Width: _____ mm (spec: _____ mm ± _____ mm)
- [ ] Épaisseur / Thickness: _____ mm (spec: _____ mm ± _____ mm)

### 4.2 Trous de fixation / Mounting Holes

- [ ] Nombre correct / Correct number: _____
- [ ] Diamètre correct / Correct diameter: _____ mm
- [ ] Position correcte / Correct position
- [ ] Entraxe conforme / Correct spacing

### 4.3 Connecteurs / Connectors

- [ ] Positions conformes au schéma / Positions conform to schematic
- [ ] Trous alignés / Holes aligned
- [ ] Espacement correct / Correct spacing

## 5. Tests électriques préliminaires / Preliminary Electrical Tests

### 5.1 Test de continuité / Continuity Test

- [ ] VCC et GND isolés (circuit ouvert) / VCC and GND isolated (open circuit)
  - Résistance mesurée / Measured resistance: _____ MΩ (> 10 MΩ attendu / expected)
- [ ] Broches adjacentes isolées / Adjacent pins isolated
- [ ] Points test accessibles / Test points accessible

### 5.2 Test d'isolation / Isolation Test

**Entre les rails d'alimentation / Between power rails:**

| Rail 1 | Rail 2 | Résistance / Resistance | Statut / Status |
|--------|--------|------------------------|-----------------|
| VCC    | GND    | _____ MΩ               | ☐ PASS ☐ FAIL  |
| 5V     | GND    | _____ MΩ               | ☐ PASS ☐ FAIL  |
| 3.3V   | GND    | _____ MΩ               | ☐ PASS ☐ FAIL  |
| 5V     | 3.3V   | _____ MΩ               | ☐ PASS ☐ FAIL  |

**Valeur minimale acceptable / Minimum acceptable value:** > 1 MΩ

## 6. Documentation / Documentation

### 6.1 Photos prises / Photos Taken

- [ ] Vue d'ensemble recto / Top side overview
- [ ] Vue d'ensemble verso / Bottom side overview
- [ ] Zones critiques (gros plans) / Critical areas (close-ups)
- [ ] Défauts éventuels / Any defects

### 6.2 Documents vérifiés / Documents Verified

- [ ] Schéma électrique / Electrical schematic
- [ ] Plan de placement des composants / Component placement plan
- [ ] Bill of Materials (BOM)
- [ ] Spécifications techniques / Technical specifications
- [ ] Certificat de conformité / Certificate of conformity

## 7. Résultat de l'inspection / Inspection Result

### 7.1 Défauts identifiés / Identified Defects

**Nombre de défauts majeurs / Number of major defects:** _____

**Nombre de défauts mineurs / Number of minor defects:** _____

**Description des défauts / Defect description:**
_______________________________________________________
_______________________________________________________
_______________________________________________________

### 7.2 Décision / Decision

- [ ] **ACCEPTÉ** / **ACCEPTED** - PCB conforme, peut passer à l'étape de soudure
  PCB compliant, can proceed to soldering step
  
- [ ] **ACCEPTÉ AVEC RÉSERVE** / **ACCEPTED WITH RESERVATION** - Défauts mineurs notés mais PCB utilisable
  Minor defects noted but PCB usable
  
- [ ] **REFUSÉ** / **REJECTED** - PCB non conforme, doit être retourné ou mis au rebut
  PCB non-compliant, must be returned or scrapped

**Justification / Justification:**
_______________________________________________________
_______________________________________________________

## 8. Actions requises / Required Actions

- [ ] Aucune action nécessaire / No action needed
- [ ] Contacter le fournisseur / Contact supplier
- [ ] Demander un remplacement / Request replacement
- [ ] Procéder à la soudure / Proceed to soldering
- [ ] Autre / Other: _______________________________

## 9. Signatures / Signatures

**Inspecteur / Inspector:** _______________  **Date:** _______________

**Responsable technique / Technical Manager:** _______________  **Date:** _______________

---

**Remarques additionnelles / Additional Remarks:**
_______________________________________________________
_______________________________________________________
_______________________________________________________
