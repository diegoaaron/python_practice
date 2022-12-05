import express from 'express';
import {pool} from './db.js';
const app = express();

app.get('/ping', async (req,res) => {
    const [result] = await pool.query('SELECT 1 + 1 as result');
    res.json(result[0]);
});

app.get('/employees', (req,res) => res.send('obteniendo empleados'));

app.post('/employees', (req,res) => res.send('creando empleados'));

app.put('/employees', (req,res) => res.send('actualizando empleados'));

app.delete('/employees', (req,res) => res.send('eliminando empleado'));

app.listen(3000);
console.log('servidor ejecutandose en puerto 3000');