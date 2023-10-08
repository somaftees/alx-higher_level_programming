#!/usr/bin/python3
def no_c(my_string):
    cpy = ''
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            cpy += my_string[i]
    return cpy
