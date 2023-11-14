#!/usr/bin/node
const dict = require('./101-data.js').dict;

const keys = Object.keys(dict);
const values = Object.values(dict);

const resultObject = {};
for (let i = 0; i < values.length; i++) {
  if (!Object.prototype.hasOwnProperty.call(resultObject, values[i])) {
    resultObject[values[i]] = [keys[i]];
  } else {
    resultObject[values[i]] = [...resultObject[values[i]], keys[i]];
  }
}
console.log(resultObject);
