#!/usr/bin/python3
"""function."""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
