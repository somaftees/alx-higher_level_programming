#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        d = 0
        for tup in my_list:
            n += (tup[0] * tup[1])
            d += tup[1]
        return (n / d)
    return 0
