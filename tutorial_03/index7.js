const express = require('express');

const app = express();

app.get('/profile', (req, res) => {
    res.send('profile page');
});

app.listen(3000);
console.log('server en puerto 3000');