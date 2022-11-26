const express = require('express');

const app = express();

app.get('/hello/:user', (req, res) => {
    console.log(req.params);
    console.log(typeof req.params.user);
    res.send(`hello ${req.params.user.toUpperCase()}`);
});

app.get('/add/:x/:y', (req, res) => {

    // utilizando la desectructracion de JS
    const {x, y} = req.params;
    res.send(`resultado: ${parseInt(x) + parseInt(y)}`);
})

app.listen(3000);
console.log('servidor en puerto 3000');