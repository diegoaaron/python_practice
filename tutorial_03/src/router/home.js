const express = require('express');

//router
const app = express.Router();

app.get('/', (req,res) => {
    const title = 'Inicio';
    res.render('index',{title});
});

app.get('/about', (req,res) => {
    const title = 'Mi pagina creada desde express';
    res.render('about');
});

app.get('/dashboard', (req, res) => {
    res.render('dashboard');
});

//exportando router
module.exports = app;