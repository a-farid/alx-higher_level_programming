#!/usr/bin/node
const myVar = process.argv;
let arrNumber = myVar
  .slice(2)
  .map((n) => Number(n))
  .sort((a, b) => b - a);
if (arrNumber[1] == undefined) {
  console.log(0);
} else {
  console.log(arrNumber[1]);
}

