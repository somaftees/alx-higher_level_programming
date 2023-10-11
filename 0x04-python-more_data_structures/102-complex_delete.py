#!/usr/bin/python3
def complex_delete(my_dict, value):
    del_keys = []
    for key in my_dict:
        if my_dict[key] == value:
            del_keys.append(key)
    for key in del_keys:
        del my_dict[key]
    return my_dict
