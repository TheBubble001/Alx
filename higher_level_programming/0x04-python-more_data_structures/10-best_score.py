#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        li = []
        for elem in sorted(a_dictionary.items(), key=lambda x: x[1]):
            li.append(elem[0])
        return li[-1]
