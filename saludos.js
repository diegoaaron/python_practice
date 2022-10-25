function saludar(nombre) {
    return `hola, ${nombre}`;
}

function saludarHolamundo() {
    return 'hola mundo';
}

module.exports.saludar = saludar;
module.exports.saludarHolamundo = saludarHolamundo;