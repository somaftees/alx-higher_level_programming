#!/usr/bin/env python3
def no_c(my_string):
    x = ''
    for i in range(len(my_string)):
        if i != 'c' and i != 'C':
            x += my_string
    return x
