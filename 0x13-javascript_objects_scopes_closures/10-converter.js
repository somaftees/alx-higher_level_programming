#!/usr/bin/node

// I hate comments.

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
