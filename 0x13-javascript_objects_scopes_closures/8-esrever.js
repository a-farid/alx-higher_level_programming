#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((acc, curr) => {
    acc.unshift(curr);
    return acc;
  }, []);
};
