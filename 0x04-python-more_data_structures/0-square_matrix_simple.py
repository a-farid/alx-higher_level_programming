#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    A function that computes the square
    value of all integers of the matrix.
    """
    new_matrix = []
    for col in matrix:
        result = [x*x for x in col]
        new_matrix.append(result)
    return new_matrix
