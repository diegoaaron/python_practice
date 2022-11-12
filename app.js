const express = require('express');

const app = express();

const {infoCursos} = require('./cursos.js'); // obteniendo los archivos con sintaxis de desestructuracion


// Routing

app.get('/', (req, res) => {
    res.send('Mi primer servidor con express. Cursos');
});

app.get('/api/cursos', (req, res) => {
    //res.send(infoCursos); // formato normal
    res.send(JSON.stringify(infoCursos)); // formato JSON
});

app.get('/api/cursos/programacion', (req, res) => {
    res.send(JSON.stringify(infoCursos.programacion));
});

app.get('/api/cursos/matematicas', (req,res) => {
    res.send(JSON.stringify(infoCursos.matematicas));
});

// puerto 
const PUERTO = process.env.PORT || 3000;

app.listen(PUERTO, () => {
    console.log(`El servidor esta escuchando en el puerto ${PUERTO}...`);
});

