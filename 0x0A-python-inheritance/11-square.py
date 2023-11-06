#!/usr/bin/python3
"""square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        """__init__"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """__str__"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
