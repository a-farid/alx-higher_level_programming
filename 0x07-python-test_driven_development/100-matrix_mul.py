#!/usr/bin/python3
""" This module with a function multiply 2 matrices """


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices.

    Args:
        m_a: matrix a.
        m_b: matrix b.

    Returns:
        multiplication of two matrix.

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elem in m_a:
        if not isinstance(elem, list):
            raise TypeError("m_a must be a list of lists")

    for elem in m_b:
        if not isinstance(elem, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for e in lists:
            if not type(e) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for e in lists:
            if not type(e) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    leng = 0
    for elem in m_a:
        if leng != 0 and leng != len(elem):
            raise TypeError("each row of m_a must be of the same size")
        leng = len(elem)

    leng = 0
    for elem in m_b:
        if leng != 0 and leng != len(elem):
            raise TypeError("each row of m_b must be of the same size")
        leng = len(elem)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    i = 0

    for a in m_a:
        m_tmp = []
        j = 0
        k = 0
        while (j < len(m_b[0])):
            k += a[i] * m_b[i][j]
            if i == len(m_b) - 1:
                i = 0
                j += 1
                m_tmp.append(k)
                k = 0
            else:
                i += 1
        res.append(m_tmp)

    return res
