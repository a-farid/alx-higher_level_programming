#!/usr/bin/node
const myVar = process.argv;
const add = (a, b) => {return a + b};
console.log(add(Number(myVar[2]), Number(myVar[3])));

