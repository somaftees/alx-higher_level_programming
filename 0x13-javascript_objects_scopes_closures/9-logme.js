#!/usr/bin/node

// I hate comments.

let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
