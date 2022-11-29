const express = require('express');

//router
const app = express.Router();

app.get('/', (req,res) => {
    let isActive = true;

    const users = [
        {
            id: 1,
            name: "ryan",
            lastname: "perez"
        },
        {
            id: 2,
            name: "luis",
            lastname: "aguilar"
        }
    ]

    res.render('index',{title: 'Index page', isActive: isActive, users: users});
});

app.get('/about', (req,res) => {
    const title = 'Mi pagina creada desde express';
    res.render('about');
});

app.get('/dashboard', (req, res) => {
    res.render('dashboard');
});

app.get('/posts', (req, res) => {
    res.render('posts');
});

//exportando router
module.exports = app;