import express from 'express';

const app = express();


app.get('/employees', (req,res) => res.send('obteniendo empleados'));

app.post('/employees', (req,res) => res.send('creando empleados'));

app.put('/employees', (req,res) => res.send('actualizando empleados'));

app.delete('/employees', (req,res) => res.send('eliminando empleado'));

app.listen(3000);
console.log('servidor ejecutandose en puerto 3000');