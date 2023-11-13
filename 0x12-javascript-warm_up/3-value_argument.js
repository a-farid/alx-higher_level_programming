#!/usr/bin/node
const argvLen = process.argv;

if (argvLen[2]) {
  console.log(argvLen[2]);
} else {
  console.log('No argument');
}

