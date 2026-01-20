// Simulation de données utilisateurs
let users = [
  { id: 1, name: 'Jean Dupont', email: 'jean.dupont@example.com' },
  { id: 2, name: 'Marie Martin', email: 'marie.martin@example.com' },
  { id: 3, name: 'Pierre Durand', email: 'pierre.durand@example.com' }
];

// GET /api/users - Récupérer tous les utilisateurs
const getUsers = (req, res) => {
  res.json({
    success: true,
    data: users,
    count: users.length
  });
};

// GET /api/users/:id - Récupérer un utilisateur par ID
const getUserById = (req, res) => {
  const id = parseInt(req.params.id);
  const user = users.find(u => u.id === id);
  
  if (!user) {
    return res.status(404).json({
      success: false,
      message: 'Utilisateur non trouvé'
    });
  }
  
  res.json({
    success: true,
    data: user
  });
};

// POST /api/users - Créer un nouvel utilisateur
const createUser = (req, res) => {
  const { name, email } = req.body;
  
  if (!name || !email) {
    return res.status(400).json({
      success: false,
      message: 'Les champs name et email sont requis'
    });
  }
  
  const newUser = {
    id: users.length > 0 ? Math.max(...users.map(u => u.id || 0)) + 1 : 1,
    name,
    email
  };
  
  users.push(newUser);
  
  res.status(201).json({
    success: true,
    message: 'Utilisateur créé avec succès',
    data: newUser
  });
};

// PUT /api/users/:id - Mettre à jour un utilisateur
const updateUser = (req, res) => {
  const id = parseInt(req.params.id);
  const { name, email } = req.body;
  const userIndex = users.findIndex(u => u.id === id);
  
  if (userIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Utilisateur non trouvé'
    });
  }
  
  if (name) users[userIndex].name = name;
  if (email) users[userIndex].email = email;
  
  res.json({
    success: true,
    message: 'Utilisateur mis à jour avec succès',
    data: users[userIndex]
  });
};

// DELETE /api/users/:id - Supprimer un utilisateur
const deleteUser = (req, res) => {
  const id = parseInt(req.params.id);
  const userIndex = users.findIndex(u => u.id === id);
  
  if (userIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Utilisateur non trouvé'
    });
  }
  
  const deletedUser = users.splice(userIndex, 1)[0];
  
  res.json({
    success: true,
    message: 'Utilisateur supprimé avec succès',
    data: deletedUser
  });
};

module.exports = {
  getUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser
};
