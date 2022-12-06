import express from 'express';


import employeesRoutes from './routes/employees.routes.js';
import indexRoutes from './routes/index.router.js';

const app = express();

app.use(express.json());

app.use(indexRoutes);
app.use('/api',employeesRoutes);

// midleware
app.use((req, res, next) => {
    res.status(404).json({
        message: 'endpoint not found'
    });
});

app.listen(3000);
console.log('servidor ejecutandose en puerto 3000');