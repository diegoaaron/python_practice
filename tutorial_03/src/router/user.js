const express = require('express');

//router
const app = express.Router();

app.get('UserName', (req,res) => {
    res.send('Username route');
});

app.get('profile', (req,res) => {
    console.log(req.body);
    res.send('profile page');
});

// exportando router
module.exports = app;