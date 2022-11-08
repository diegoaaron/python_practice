const { Console } = require('console');
const http = require('http');

const cursos = require('./cursos.js');

const servidor = http.createServer((req, res) => {
    const {method} = req;

    switch(method) {
        case 'GET':
            return manejarSolicitudGET(req, res);
        case 'POST':
            return manejarSolicitudPOST(req, res);
        case 'DELETE':
            return manejarSolicitudDELETE(req, res);
        default:
            console.log(`El metodo utilizado no puede ser manejado por el servido: ${method}`);
    }
});

function manejarSolicitudGET(req, res) {
    const path = req.url;

    if(path === '/') {
        res.statusCode = 200;
        return res.end('Bienvenido a mi primer servidor y API creado con Nodejs');
    } else if (path === '/cursos') {
        res.statusCode = 200;
        return res.end(JSON.stringify(cursos.infoCursos));
    } else if (path == '/cursos/programacion') {
        res.statusCode = 200;
        return res.end(JSON.stringify(cursos.infoCursos.programacion));
    }

    res.statusCode = 404;
    return res.end('El recurso solicitado, no existe...');
}

function manejarSolicitudPOST(req, res) {
    const path = req.url;

    if (path === '/cursos/programacion') {
        res.statusCode = 200;
        return res.end('El servidor recibio una solicitud POST para /cursos/programacion');
    }
}

function manejarSolicitudDELETE(req, res) {
    const path = req.url;

    if (path === '/cursos/programacion') {
        res.statusCode = 200;
        return res.end('El servidor recbio una solicitud DELETE para /cursos/programacion');
    }
}

const PUERTO = 3000;

servidor.listen(PUERTO, () => {
    console.log(`El servidor esta escuchando en el puerto ${PUERTO}`);
})