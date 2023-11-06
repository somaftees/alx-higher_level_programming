#!/usr/bin/python3
"""class"""


class MyInt(int):
    """MyInt"""
    def __init__(self, num):
        """__init__"""
        self.num = num

    def __eq__(self, other):
        """__eq__"""
        return self.num != other

    def __ne__(self, other):
        """__ne__"""
        return self.num == other
