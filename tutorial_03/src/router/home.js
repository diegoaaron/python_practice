const express = require('express');

//router
const app = express.Router();

app.all('/about', (req,res) => {

    const title = 'Mi pagina creada desde express';

    res.render('index', {title});
});

app.get('/dashboard', (req, res) => {
    res.send('dashboard page');
});

//exportando router
module.exports = app;