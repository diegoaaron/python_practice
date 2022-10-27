const curso = require('./curso.json');

console.log(typeof curso);

console.log(curso.titulo);

let infoCurso = {
    "titulo": "aprende node.js",
    "numVistas": 45625,
    "numLikes": 21123,
    "temas": [
      "javascript",
      "node.js"
    ],
    "esPublico": true
  }

  console.log(infoCurso);