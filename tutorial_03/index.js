const express =require('express');

const app = express();

app.get('/',(req, res) => {
    res.send('hello world');
});

app.get('/about',(req, res) => {
    res.send('About');
});

app.get('/weather',(req, res) => {
    res.send('the current weather is nice');
});

app.listen(3000);
console.log(`server en puerto ${3000}`);

