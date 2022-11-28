const express = require('express');
const morgan = require('morgan');

const app = express();

let products = [{
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


// PUT 
app.put('/products/:id', (req,res) => {

    const newData = req.body

    const productFound = products.find((product) => product.id === parseInt(req.params.id));

    if (!productFound) return res.status(404).json({
        message: "Producto no encontrado"
    });

    products = products.map(p => p.id === parseInt(req.params.id) ? {...p, ...newData} : p);

    console.log(products);
    res.json({
        message: "Producto actualizado"
    });
});


// DELETE
app.delete('/products/:id', (req,res) => {

    const productFound = products.find((product) => product.id === parseInt(req.params.id));

    if (!productFound) return res.status(404).json({
        message: "Producto no encontrado"
    });

    products = products.filter(p => p.id !== parseInt(req.params.id));

    res.sendStatus(404);
});


// GET ID
app.get('/products/:id', (req,res) => {
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