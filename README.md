# 2526_B3_S6_Projet

Projet B3 S6 - Système embarqué avec composants multiples

## Modules

### Filtrage
Module de filtrage numérique pour le traitement de signaux. Fournit des implémentations de filtres passe-bas, passe-haut, passe-bande et à moyenne mobile.

Voir [filtrage/README.md](filtrage/README.md) pour plus de détails.

## Structure du projet

```
.
├── filtrage/          # Module de filtrage de signaux
│   ├── filters.py     # Implémentations des filtres
│   ├── example.py     # Exemples d'utilisation
│   ├── test_filters.py # Tests
│   └── README.md      # Documentation du module
└── README.md          # Ce fichier
```

## Utilisation

Pour utiliser le module de filtrage :

```python
from filtrage import LowPassFilter

# Créer un filtre passe-bas
lpf = LowPassFilter(alpha=0.3)

# Filtrer des données
filtered_value = lpf.filter(sensor_reading)
```

Voir `filtrage/example.py` pour des exemples complets.

## Tests

Pour tester le module de filtrage :

```bash
python filtrage/test_filters.py
```

## License

Ce projet fait partie du cursus académique B3 S6.