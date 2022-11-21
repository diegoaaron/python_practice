const EventEmitter = require('events');

const customEmitter = new EventEmitter();

customEmitter.on('response', (data) => {
    console.log('recibido');
    console.log(data);
});

// emitiendo 

customEmitter.emit('response','hello word');