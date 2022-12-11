// importar mysql
import mysql from 'mysql';

// crear la conexion
const conector = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'diego989',
    database: 'agenda_contacto'
});

const conectar = () => {
    conector.connect(err => {
        if(err) throw err
        console.log('conectado');
    });
}

export {conectar}

/**
 * user: root
 * pass: diego989
 * database: agenda_contacto
 * tabla: agenda
 */