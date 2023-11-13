#!/usr/bin/node
const argvLen = process.argv.length;

if (argvLen === 3) {
  console.log('Argument found');
} else if (argvLen === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
