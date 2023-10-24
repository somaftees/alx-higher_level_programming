#!/usr/bin/python3
"""a class square"""


class Square:
    """squre"""
    def __init__(self, size=0):
        """init the squre"""
        if type(size) is not int:
            raise TypeError("size is not an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area"""
        return self.__size ** 2
