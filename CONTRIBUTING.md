# Guide de Contribution / Contributing Guide

## Français

### Comment contribuer au projet

Ce projet est un projet académique B3 S6. Les contributions sont les bienvenues dans les limites du cadre académique.

#### Structure du projet

Le projet est organisé en modules indépendants :
- **asservi/** : Module d'asservissement PID
- **filtrage/** : Module de filtrage de signal
- **hardware/pcb/** : Fichiers de conception PCB
- **src/** : Application principale
- **tests/** : Tests unitaires

#### Workflow de développement

1. **Fork** le dépôt
2. **Créer une branche** pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`)
3. **Faire vos modifications** en suivant les standards de code
4. **Tester** vos modifications
5. **Commiter** vos changements (`git commit -m 'Ajout de ma fonctionnalité'`)
6. **Push** vers la branche (`git push origin feature/ma-fonctionnalite`)
7. **Ouvrir une Pull Request**

#### Standards de code

- **Python** : Suivre PEP 8
- **Documentation** : Documenter toutes les fonctions publiques
- **Tests** : Ajouter des tests pour les nouvelles fonctionnalités
- **Commits** : Messages de commit clairs et descriptifs

#### Ajouter un nouveau module

1. Créer un nouveau répertoire pour le module
2. Ajouter `__init__.py` avec les exports
3. Créer un `README.md` avec la documentation
4. Ajouter des exemples d'utilisation
5. Ajouter des tests si applicable
6. Mettre à jour le README principal

#### Tests

Avant de soumettre une PR, assurez-vous que tous les tests passent :

```bash
# Test du module principal
python tests/test_main.py

# Test du module filtrage
python filtrage/test_filters.py

# Test de l'application complète
python src/main.py
```

---

## English

### How to contribute to the project

This is a B3 S6 academic project. Contributions are welcome within the academic framework.

#### Project Structure

The project is organized into independent modules:
- **asservi/** : PID servo control module
- **filtrage/** : Signal filtering module
- **hardware/pcb/** : PCB design files
- **src/** : Main application
- **tests/** : Unit tests

#### Development Workflow

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b feature/my-feature`)
3. **Make your changes** following code standards
4. **Test** your changes
5. **Commit** your changes (`git commit -m 'Add my feature'`)
6. **Push** to the branch (`git push origin feature/my-feature`)
7. **Open a Pull Request**

#### Code Standards

- **Python** : Follow PEP 8
- **Documentation** : Document all public functions
- **Tests** : Add tests for new features
- **Commits** : Clear and descriptive commit messages

#### Adding a New Module

1. Create a new directory for the module
2. Add `__init__.py` with exports
3. Create a `README.md` with documentation
4. Add usage examples
5. Add tests if applicable
6. Update the main README

#### Testing

Before submitting a PR, make sure all tests pass:

```bash
# Test main module
python tests/test_main.py

# Test filtrage module
python filtrage/test_filters.py

# Test complete application
python src/main.py
```

## Contributors / Contributeurs

- **BNightymare** - Project Lead / Chef de projet
- **Samirtaza** - Development / Développement
- **Lucie913** - Development / Développement

## Questions

Pour toute question, ouvrez une issue sur GitHub.

For any questions, open an issue on GitHub.
