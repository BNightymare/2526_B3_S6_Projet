const express = require('express');
const router = express.Router();
const homeController = require('../controllers/homeController');
const userController = require('../controllers/userController');
const productController = require('../controllers/productController');

// Route principale
router.get('/', homeController.home);
router.get('/about', homeController.about);

// Routes API pour les utilisateurs
router.get('/api/users', userController.getUsers);
router.get('/api/users/:id', userController.getUserById);
router.post('/api/users', userController.createUser);
router.put('/api/users/:id', userController.updateUser);
router.delete('/api/users/:id', userController.deleteUser);

// Routes API pour les produits
router.get('/api/products', productController.getProducts);
router.get('/api/products/:id', productController.getProductById);
router.post('/api/products', productController.createProduct);
router.put('/api/products/:id', productController.updateProduct);
router.delete('/api/products/:id', productController.deleteProduct);

module.exports = router;
