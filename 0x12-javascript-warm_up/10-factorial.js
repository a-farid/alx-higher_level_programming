#!/usr/bin/node
const myVar = process.argv[2];
let result = 1;

for (let i = 1; i <= myVar; i++) result *= i;

console.log(result);

