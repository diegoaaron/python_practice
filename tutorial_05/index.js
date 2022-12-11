import express from 'express';

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
    res.render('index', {titulo:'aplicacion de contactos', dato:'cualquier texto'});
});



// configuracion del peruto
app.listen('8000', function() {
    console.log('aplicacion iniciada en el puerto 8000');
});


