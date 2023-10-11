#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        m = list(my_dict.keys())[0]
        for key in my_dict:
            if my_dict[key] > my_dict[max]:
                m = key
        return m
    return None
