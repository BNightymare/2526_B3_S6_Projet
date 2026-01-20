# 2526_B3_S6_Projet - Système de Routage

Projet académique de routage avec Express.js pour démontrer la mise en place d'un système de routage RESTful complet.

## 📋 Description

Ce projet implémente un système de routage moderne avec Express.js, incluant :
- Routes RESTful pour la gestion d'utilisateurs et de produits
- Middleware de journalisation et de gestion d'erreurs
- Architecture MVC (Model-View-Controller)
- API JSON complète

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/BNightymare/2526_B3_S6_Projet.git
cd 2526_B3_S6_Projet

# Installer les dépendances
npm install
```

## 💻 Utilisation

### Démarrer le serveur

```bash
# Mode production
npm start

# Mode développement (avec rechargement automatique)
npm run dev
```

Le serveur démarre sur `http://localhost:3000`

## 🛣️ Routes disponibles

### Routes principales
- `GET /` - Page d'accueil avec la liste des endpoints disponibles
- `GET /about` - Informations sur le projet

### Routes API - Utilisateurs
- `GET /api/users` - Récupérer tous les utilisateurs
- `GET /api/users/:id` - Récupérer un utilisateur spécifique
- `POST /api/users` - Créer un nouvel utilisateur
- `PUT /api/users/:id` - Mettre à jour un utilisateur
- `DELETE /api/users/:id` - Supprimer un utilisateur

### Routes API - Produits
- `GET /api/products` - Récupérer tous les produits
- `GET /api/products/:id` - Récupérer un produit spécifique
- `POST /api/products` - Créer un nouveau produit
- `PUT /api/products/:id` - Mettre à jour un produit
- `DELETE /api/products/:id` - Supprimer un produit

## 📝 Exemples d'utilisation

### Récupérer tous les utilisateurs
```bash
curl http://localhost:3000/api/users
```

### Créer un utilisateur
```bash
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Dubois", "email": "alice.dubois@example.com"}'
```

### Mettre à jour un produit
```bash
curl -X PUT http://localhost:3000/api/products/1 \
  -H "Content-Type: application/json" \
  -d '{"price": 899.99, "stock": 15}'
```

## 🏗️ Structure du projet

```
2526_B3_S6_Projet/
├── src/
│   ├── index.js                 # Point d'entrée de l'application
│   ├── routes/
│   │   └── index.js             # Configuration des routes
│   ├── controllers/
│   │   ├── homeController.js    # Contrôleur des pages principales
│   │   ├── userController.js    # Contrôleur des utilisateurs
│   │   └── productController.js # Contrôleur des produits
│   └── middleware/
│       ├── logger.js            # Middleware de journalisation
│       └── errorHandler.js      # Middleware de gestion d'erreurs
├── package.json
└── README.md
```

## 🔧 Technologies utilisées

- **Node.js** - Environnement d'exécution JavaScript
- **Express.js** - Framework web minimaliste
- **CORS** - Middleware pour gérer les requêtes cross-origin
- **Nodemon** - Outil de développement pour le rechargement automatique

## 📚 Concepts de routage

Ce projet démontre :
- **Routage RESTful** : Organisation des routes selon les principes REST
- **Middleware** : Utilisation de middleware pour la journalisation et la gestion d'erreurs
- **Architecture MVC** : Séparation claire entre routes, contrôleurs et logique métier
- **Gestion d'erreurs** : Middleware centralisé pour gérer les erreurs et les routes non trouvées
- **Paramètres de route** : Utilisation de paramètres dynamiques dans les URLs

## 👨‍💻 Auteur

BNightymare

## 📄 Licence

ISC