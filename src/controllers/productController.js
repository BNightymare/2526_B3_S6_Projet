// Simulation de données produits
let products = [
  { id: 1, name: 'Ordinateur portable', price: 999.99, stock: 10 },
  { id: 2, name: 'Souris sans fil', price: 29.99, stock: 50 },
  { id: 3, name: 'Clavier mécanique', price: 89.99, stock: 25 }
];

// GET /api/products - Récupérer tous les produits
const getProducts = (req, res) => {
  res.json({
    success: true,
    data: products,
    count: products.length
  });
};

// GET /api/products/:id - Récupérer un produit par ID
const getProductById = (req, res) => {
  const id = parseInt(req.params.id);
  const product = products.find(p => p.id === id);
  
  if (!product) {
    return res.status(404).json({
      success: false,
      message: 'Produit non trouvé'
    });
  }
  
  res.json({
    success: true,
    data: product
  });
};

// POST /api/products - Créer un nouveau produit
const createProduct = (req, res) => {
  const { name, price, stock } = req.body;
  
  if (!name || typeof price === 'undefined' || typeof stock === 'undefined') {
    return res.status(400).json({
      success: false,
      message: 'Les champs name, price et stock sont requis'
    });
  }
  
  const parsedPrice = parseFloat(price);
  const parsedStock = parseInt(stock, 10);
  
  if (isNaN(parsedPrice) || parsedPrice < 0) {
    return res.status(400).json({
      success: false,
      message: 'Le prix doit être un nombre valide >= 0'
    });
  }
  
  if (isNaN(parsedStock) || parsedStock < 0) {
    return res.status(400).json({
      success: false,
      message: 'Le stock doit être un nombre entier valide >= 0'
    });
  }
  
  const newProduct = {
    id: products.length > 0 ? Math.max(...products.map(p => p.id || 0)) + 1 : 1,
    name,
    price: parsedPrice,
    stock: parsedStock
  };
  
  products.push(newProduct);
  
  res.status(201).json({
    success: true,
    message: 'Produit créé avec succès',
    data: newProduct
  });
};

// PUT /api/products/:id - Mettre à jour un produit
const updateProduct = (req, res) => {
  const id = parseInt(req.params.id);
  const { name, price, stock } = req.body;
  const productIndex = products.findIndex(p => p.id === id);
  
  if (productIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Produit non trouvé'
    });
  }
  
  if (name) products[productIndex].name = name;
  
  if (typeof price !== 'undefined') {
    const parsedPrice = parseFloat(price);
    if (isNaN(parsedPrice) || parsedPrice < 0) {
      return res.status(400).json({
        success: false,
        message: 'Le prix doit être un nombre valide >= 0'
      });
    }
    products[productIndex].price = parsedPrice;
  }
  
  if (typeof stock !== 'undefined') {
    const parsedStock = parseInt(stock, 10);
    if (isNaN(parsedStock) || parsedStock < 0) {
      return res.status(400).json({
        success: false,
        message: 'Le stock doit être un nombre entier valide >= 0'
      });
    }
    products[productIndex].stock = parsedStock;
  }
  
  res.json({
    success: true,
    message: 'Produit mis à jour avec succès',
    data: products[productIndex]
  });
};

// DELETE /api/products/:id - Supprimer un produit
const deleteProduct = (req, res) => {
  const id = parseInt(req.params.id);
  const productIndex = products.findIndex(p => p.id === id);
  
  if (productIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Produit non trouvé'
    });
  }
  
  const deletedProduct = products.splice(productIndex, 1)[0];
  
  res.json({
    success: true,
    message: 'Produit supprimé avec succès',
    data: deletedProduct
  });
};

module.exports = {
  getProducts,
  getProductById,
  createProduct,
  updateProduct,
  deleteProduct
};
