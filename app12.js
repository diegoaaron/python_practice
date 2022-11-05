const http = require('http');

const servidor = http.createServer((req, res) => {
    console.log('===> req(solicitud)');
    console.log(req.url);
    console.log(req.method);
    console.log(req.headers);
    res.end('hola mundo');
});

const PUERTO = 3000;

servidor.listen(PUERTO, () => {
    console.log(`El servidor esta escuchando en el puerto ${PUERTO}`);
});
