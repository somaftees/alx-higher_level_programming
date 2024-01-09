#!/usr/bin/node

// I hate comments.

const arr = require('./100-data').list;

console.log(arr);
console.log(arr.map((x, idx) => x * idx));
