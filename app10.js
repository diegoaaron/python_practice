function ordenarProducto(producto) {
  return new Promise((resolve, reject) => {
    console.log(`Ordenando: ${producto} de freecodeCampa`);
    setTimeout(() => {
      if(producto === 'taza') {
        resolve('Ordenando una taza con el logo de freeCodeCamp...');
      } else {
        reject('Este producto no esta disponible actualmente...');
      }
    }, 3000);
  });
}

function procesarPedido(respuesta) {
  return new Promise((resolve, reject) => {
    console.log('Procesando respuesta...');
    console.log(`La respuesta fue "${respuesta}"`);
    setTimeout(() => {
      resolve('Gracias por tu compra. Disfruta tu producto de freeCodeCamp');
    }, 4000);
  });
}

ordenarProducto('taza')
  .then(respuesta => {
    console.log('Respuesta recibida');
    console.log(respuesta)
  })