const express = require('express');

const {matematicas} = require('../datos/cursos.js');

const routerMatematicas = express.Router();


// ruta con parametro matemáticas

routerMatematicas.get('/', (req,res) => {
    res.send(JSON.stringify(matematicas));
});

routerMatematicas.get('/:tema', (req, res) => {
    const tema = req.params.tema;

    const resultados = matematicas.filter(curso => curso.tema === tema);

    if (resultados.length === 0) {
        return res.status(404).send(`No se encontro curso de ${lenguaje}`);
    }

    res.send(JSON.stringify(resultados));
});