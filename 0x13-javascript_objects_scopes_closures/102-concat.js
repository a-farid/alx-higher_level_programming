#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const fromFileToFile = (source, dest) => {
  fs.readFile(`./${source}`, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading the file:', err);
    } else {
      fs.appendFile(`./${dest}`, data, (err) => {
        if (err) console.error('Error:', err);
      });
      fs.appendFile(`./${dest}`, '\n', (err) => {
        if (err) console.error('Error:', err);
      });
    }
  });
};
fromFileToFile(args[2], args[4]);
fromFileToFile(args[3], args[4]);
