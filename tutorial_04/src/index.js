import express from 'express';


import employeesRoutes from './routes/employees.routes.js';
import indexRoutes from './routes/index.router.js';

const app = express();

app.use(indexRoutes);
app.use(employeesRoutes);

app.listen(3000);
console.log('servidor ejecutandose en puerto 3000');