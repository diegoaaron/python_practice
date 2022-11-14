let username = 'fast';

let age = 14;

let hasHobbies = false;

let points = [10,20,30];

let user = {
    name: 'diego',
    lastname: 'ray'
}

const PI = 3.1415;

console.log(username);
console.log(age);
console.log(hasHobbies);
console.log(points);
console.log(user);


if(age >= 18) {
    console.log("eres un adulto");
} else if(age >= 13) {
    console.log("eres un adolecente");
} else {
    console.log("eres un niño");
}

const otrosNombres = ['joe','jhon','luis'];

for(let i = 0; i< otrosNombres.length; i++) {
    console.log(otrosNombres[i]);
}

function showUserInfo(username, userage) {
    return `el usuario tiene ${username} con ${userage}`;
}

console.log(showUserInfo('diego',31));

const haber = (username, userage) => `el usuario tiene ${username} con ${userage}`;

console.log(haber('liz',22));