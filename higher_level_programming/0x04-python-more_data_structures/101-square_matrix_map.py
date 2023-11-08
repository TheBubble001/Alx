#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda mem: list(map(lambda el: el * el, mem)), matrix))
