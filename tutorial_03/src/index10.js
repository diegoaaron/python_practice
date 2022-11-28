const express = require("express");
const path = require('path');

const app = express();

//settings
app.use("/public",express.static(path.join(__dirname,'public')))
app.use("/uploads",express.static(path.join(__dirname,'uploads')))

// GET
app.get("/profile", (req, res) => {
  res.send("web perfil");
});

app.get("/note.txt", (req, res) => {
    res.send("este no es un archivo note.txt");
  });

app.listen(3000);
console.log(`server en puerto ${3000}`);
