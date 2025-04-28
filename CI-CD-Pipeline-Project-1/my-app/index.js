const express = require('express');
const app = express();

// Import user routes
const userRoutes = require('./routes/user');

// Middleware to use user routes
app.use('/api/user', userRoutes);

app.get('/', (req, res) => {
  res.send('Hello from Dockerized Node.js App!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
