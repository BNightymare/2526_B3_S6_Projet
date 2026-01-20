# Filtrage - Signal Filtering Module

Module de filtrage numérique pour le traitement de signaux.

## Description

Ce module fournit des implémentations de filtres numériques couramment utilisés pour le traitement du signal :

- **MovingAverageFilter** : Filtre à moyenne mobile pour lisser les signaux
- **LowPassFilter** : Filtre passe-bas pour atténuer les hautes fréquences
- **HighPassFilter** : Filtre passe-haut pour atténuer les basses fréquences
- **BandPassFilter** : Filtre passe-bande combinant passe-bas et passe-haut

## Utilisation

### Installation

Aucune dépendance externe n'est requise. Le module utilise uniquement la bibliothèque standard Python.

### Exemples

#### Filtre à moyenne mobile

```python
from filtrage import MovingAverageFilter

# Créer un filtre avec une fenêtre de 5 échantillons
ma_filter = MovingAverageFilter(window_size=5)

# Appliquer le filtre à des valeurs individuelles
filtered_value = ma_filter.filter(10.5)

# Ou appliquer à un signal complet
from filtrage.filters import apply_filter_to_signal
signal = [1.0, 2.0, 3.0, 4.0, 5.0]
filtered_signal = apply_filter_to_signal(signal, ma_filter)
```

#### Filtre passe-bas

```python
from filtrage import LowPassFilter

# Créer un filtre passe-bas avec alpha=0.3 (plus de lissage)
lpf = LowPassFilter(alpha=0.3)

# Appliquer le filtre
for value in sensor_data:
    filtered_value = lpf.filter(value)
    print(filtered_value)
```

#### Filtre passe-haut

```python
from filtrage import HighPassFilter

# Créer un filtre passe-haut
hpf = HighPassFilter(alpha=0.8)

# Filtrer le signal pour enlever la composante DC
filtered_signal = [hpf.filter(v) for v in signal]
```

#### Filtre passe-bande

```python
from filtrage import BandPassFilter

# Créer un filtre passe-bande
bpf = BandPassFilter(low_alpha=0.3, high_alpha=0.7)

# Appliquer le filtre
filtered_value = bpf.filter(noisy_signal_value)
```

## Paramètres

### MovingAverageFilter
- `window_size` : Nombre d'échantillons à moyenner (défaut: 5)

### LowPassFilter
- `alpha` : Facteur de lissage (0 < alpha <= 1)
  - Valeurs basses = plus de lissage
  - Valeurs hautes = moins de lissage, plus réactif

### HighPassFilter
- `alpha` : Coefficient du filtre (0 < alpha <= 1)
  - Valeurs basses = plus d'atténuation des basses fréquences
  - Valeurs hautes = moins d'atténuation

### BandPassFilter
- `low_alpha` : Coefficient du filtre passe-bas
- `high_alpha` : Coefficient du filtre passe-haut

## Applications

Ce module peut être utilisé pour :
- Filtrage de données de capteurs
- Réduction du bruit dans les signaux
- Traitement de signaux de contrôle
- Analyse de signaux embarqués
- Applications robotiques

## License

Ce projet fait partie du cursus académique B3 S6.
