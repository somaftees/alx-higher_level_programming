#!/usr/bin/python3
"""class"""


def add_attribute(obj, attribute, value):
    """add attribute"""
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
