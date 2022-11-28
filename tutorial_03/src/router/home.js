const express = require('express');

//router
const app = express.Router();

app.all('/about', (req,res) => {
    res.send('about page');
});

app.get('/dashboard', (req, res) => {
    res.send('dashboard page');
});

//exportando router
module.exports = app;