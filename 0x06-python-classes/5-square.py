#!/usr/bin/python3
"""a square class"""


class Square:
    """initializes the square"""
    def __init__(self, size=0):
        """square initialization"""
        self.size = size

    @property
    def size(self):
        """size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area"""
        return (self.__size ** 2)

    def my_print(self):
        """print #"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
