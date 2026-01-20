// Contrôleur pour les pages principales
const home = (req, res) => {
  res.json({
    message: 'Bienvenue sur l\'application de routage',
    endpoints: {
      home: '/',
      about: '/about',
      users: {
        list: 'GET /api/users',
        get: 'GET /api/users/:id',
        create: 'POST /api/users',
        update: 'PUT /api/users/:id',
        delete: 'DELETE /api/users/:id'
      },
      products: {
        list: 'GET /api/products',
        get: 'GET /api/products/:id',
        create: 'POST /api/products',
        update: 'PUT /api/products/:id',
        delete: 'DELETE /api/products/:id'
      }
    }
  });
};

const about = (req, res) => {
  res.json({
    name: 'Projet de routage B3 S6',
    description: 'Application démonstrative de routage avec Express.js',
    version: '1.0.0',
    author: 'BNightymare'
  });
};

module.exports = {
  home,
  about
};
