#!/usr/bin/node
const argvLen = process.argv;

if (isNaN(argvLen[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argvLen[2]}`);
}

