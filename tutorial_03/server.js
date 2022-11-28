const express = require('express');
const morgan = require('morgan');

const app = express();

const products = [{
    "id": 1,
    "name": "laptop",
    "price": 3000
}];

//midleware
app.use(morgan('dev'));
app.use(express.json());


// GET 
app.get('/products', (req,res) => {
    res.json(products);
});

// POST
app.post('/products', (req,res) => {
    const newProduct = {id: products.length + 1,...req.body};
    products.push(newProduct);
    res.send(newProduct);
});

app.put('/products', (req,res) => {
    res.send('actualizando productos');
});

app.delete('/products', (req,res) => {
    res.send('eliminando productos');
});

// GET ID
app.get('/products/:id', (req,res) => {
    console.log(req.params.id);
    const productFound = products.find((product) => {
        return product.id === parseInt(req.params.id);
    });

    if (!productFound) return res.status(404).json({
        message: "Producto no encontrado"
    });

    res.json(productFound);
});

app.listen(3000);
console.log('escuchando en 3000');