#!/usr/bin/python3
"""class"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """returns current size of the square"""
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

    def __eq__(self, other):
        """eq"""
        return self.area() == other.area()

    def __ne__(self, other):
        """area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """lt"""
        return self.area() < other.area()

    def __le__(self, other):
        """lt"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """gt"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ge"""
        return self.area() >= other.area()
