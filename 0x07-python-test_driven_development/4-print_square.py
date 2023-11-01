#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """prints square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/4-print_square.txt")
