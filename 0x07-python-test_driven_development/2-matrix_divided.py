#!/usr/bin/python3
"""This module having a function that devide all
the elements of a matrix"""


def matrix_divided(matrix, div):
    """ Function devide all the elements of a matrix.

    Args:
        matrix: list of lists.
        b: devided number.

    Returns:
        The sum of the given numbers

    Raises:
        TypeError: If an element in the matrix is
                   not integer and/or float number

    """
    # Check if matrix is list of liste:
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not all((isinstance(item, int) or isinstance(item, float)) for item in i) or len(i) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    # Check if DIV is float or integer
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    # Check if DIV iz zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Check if all the elements in the matrix are the same length
    for i in matrix:
        if not all(len(i) == len(j) for j in matrix):
            raise TypeError('Each row of the matrix must have the same size')

    res = []

    for i in matrix:
        element = []
        [element.append(round(item/div, 2)) for item in i]
        res.append(element)
    return res
