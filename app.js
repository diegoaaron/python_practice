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

// ruta con parametro PROGRAMACION

app.get('/api/cursos/programacion/:lenguaje', (req, res) => {
    const lenguaje = req.params.lenguaje;

    const resultados = infoCursos.programacion.filter(curso => curso.lenguaje === lenguaje);

    if (resultados.length === 0) {
        return res.status(404).send(`No se encontro cursos de ${lenguaje}`);
    }

    if (req.query.ordenar === 'vistas') {
        return res.send(JSON.stringify(resultados.sort((a, b) => b.vistas - a.vistas)));
    }

    res.send(JSON.stringify(resultados));
});

// ruta con parametro MATEMATICAS

app.get('/api/cursos/matematicas/:tema', (req, res) => {
    const tema = req.params.tema;

    const resultados = infoCursos.matematicas.filter(curso => curso.tema === tema);

    if (resultados.length === 0) {
        return res.status(404).send(`No se encontro curso de ${lenguaje}`);
    }

    res.send(JSON.stringify(resultados));
});

app.get('/api/cursos/programacion/:lenguaje/:nivel', (req, res) => {
    const lenguaje = req.params.lenguaje;
    const nivel = req.params.nivel;

    const resultados = infoCursos.programacion.filter(curso => curso.lenguaje === lenguaje && curso.nivel === nivel);

    if (resultados === 0) {
        return res.status(404).send(`No se encontro el curso ${lenguaje} de nivel ${nivel}`);
    }

    res.send(JSON.stringify(resultados));

});

// puerto 
const PUERTO = process.env.PORT || 3000;

app.listen(PUERTO, () => {
    console.log(`El servidor esta escuchando en el puerto ${PUERTO}...`);
});

