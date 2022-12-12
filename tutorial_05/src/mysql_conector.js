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

const agregarContacto = (numero, nombre) => {
    const sql = `INSERT INTO agenda(id_agenda, nombre_contacto, numero_contacto) VALUES(${null}, "${nombre}", ${numero})`;
    conector.query(sql, function(err, result, filed){
        if(err) throw err
        console.log(result);
    })
}

const obtenerContactos = () => {
    const sql = 'SELECT * FROM agenda';
    conector.query(sql, function(err, result, filed){
        if(err) throw err
        //console.log(result);
        return result;
    });
    
}

export {conectar, agregarContacto, obtenerContactos}

/**
 * user: root
 * pass: diego989
 * database: agenda_contacto
 * tabla: agenda
 */