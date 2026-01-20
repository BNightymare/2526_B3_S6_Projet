// Middleware de gestion d'erreurs

// Gestion des routes non trouvées
const notFoundHandler = (req, res, next) => {
  res.status(404).json({
    success: false,
    message: 'Route non trouvée',
    path: req.path
  });
};

// Gestion des erreurs
const errorHandler = (err, req, res, next) => {
  console.error('Erreur:', err);
  
  res.status(err.status || 500).json({
    success: false,
    message: err.message || 'Erreur interne du serveur',
    error: process.env.NODE_ENV === 'development' ? err.stack : undefined
  });
};

module.exports = {
  notFoundHandler,
  errorHandler
};
