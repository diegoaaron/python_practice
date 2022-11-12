const express = require('express');

const app = express();

const {infoCursos} = require('./cursos.js'); // obteniendo los archivos con sintaxis de desestructuracion


// Routing

app.get('/', (req, res) => {
    res.send('Mi primer servidor con express. Cursos');
});


// puerto 
const PUERTO = process.env.PORT || 3000;

app.listen(PUERTO, () => {
    console.log(`El servidor esta escuchando en el puerto ${PUERTO}...`);
});

