#!/usr/bin/python3
def square_matrix_simple2(matrix=[]):
    new_matrix = []
    for col in matrix:
        result = list([x*x for x in col])
        new_matrix.append(result)
    return new_matrix
