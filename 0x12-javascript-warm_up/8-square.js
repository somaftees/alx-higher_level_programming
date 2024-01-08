#!/usr/bin/node

const s = parseInt(process.argv[2]);
let j;

if (s) {
  for (let i = 0; i < s; ++i) {
    for (j = 0; j < s; ++j) {
      process.stdout.write('X');
    }

    if (j === s) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
