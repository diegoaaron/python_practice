const express = require('express');

const app= express();


app.post('/user', (req,res) => {
    res.send('nuevo usuario creado');
})

app.listen(3000);
console.log(`server en puerto ${3000}`);

