#!/usr/bin/python3
# 5-save_to_json_file.py
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
