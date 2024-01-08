#!/usr/bin/node

const l = process.argv.length;
const num = process.argv.slice(2).map(function (n) {
  return parseInt(n);
});
const max = Math.max.apply(Math, num);
const min = Math.min.apply(Math, num);

if (l > 3) {
  let i = 0;
  let j = 0;
  let r = min;

  for (; i < l; ++i) {
    j = num[i];

    if (j > r && j < max) {
      r = j;
    }
  }

  console.log(r);
} else {
  console.log(0);
}
