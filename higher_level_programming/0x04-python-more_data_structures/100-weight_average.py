#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum01 = sum1 = 0
        for elem in my_list:
            sum01 += (elem[0] * elem[1])
            sum1 += elem[1]
        return (sum01 / sum1)
    return 0
