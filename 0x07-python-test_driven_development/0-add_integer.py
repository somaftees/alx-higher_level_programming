#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/0-add_integer.txt")
