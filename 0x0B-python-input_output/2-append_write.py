#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
