#!/usr/bin/node
const argvLen = process.argv;

if (argvLen.length === 2) {
  console.log('No argument');
} else {
  console.log(argvLen[2]);
}

