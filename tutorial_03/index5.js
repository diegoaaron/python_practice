const express = require('express');

const app = express();

app.get('/hello/:user', (req, res) => {
    console.log(req.params);
    res.send(`hello ${req.params.user}`);
});

app.listen(3000);
console.log('servidor en puerto 3000');