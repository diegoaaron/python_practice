import express from 'express';
import {conectar} from './src/mysql_conector.js';

const app = express();

// configuración de pug
app.set('views', './vistas');
app.set('view engine', 'pug');

// configuracion de archivos estaticos
app.use(express.static('./vistas'))
app.use(express.static('./src'))
app.use(express.static('./css'))

// get raiz
app.get('/', (req, res) => {
    //res.send('aplicacion inidicada... todo va bien');
    conectar();
    res.render('index', {titulo:'aplicacion de contactos', dato:'cualquier texto'});
});

app.get('/agregar/:nombre/:numero', (req, res) => {
    let nombre = req.params.nombre;
    let numero = req.params.numero;
    console.log(nombre, numero);
})

// configuracion del peruto
app.listen('8000', function() {
    console.log('aplicacion iniciada en el puerto 8000');
});


