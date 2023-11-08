#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    li = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            li.append(k)
    for k in li:
        del a_dictionary[k]
    return a_dictionary
