#!/usr/bin/node
const list = require('100-data.js').list;
const listMod = list.map((i, j) => i * j);

console.log(list);
console.log(listMod);
