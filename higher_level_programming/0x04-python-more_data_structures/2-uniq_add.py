#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_sum = 0
    for n in set(my_list):
        new_sum += n
    return new_sum
