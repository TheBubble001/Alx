#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
    """
    final = []
    for n in my_list:
        if n == search:
            n = replace
        final.append(n)

    return final
