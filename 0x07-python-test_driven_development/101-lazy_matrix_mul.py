#!/usr/bin/python3.5
""" This module have a function multiply 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function multiplies 2 matrices.

    Args:
        m_a: matrix a.
        m_b: matrix b.

    Returns:
        multiplication of two matrix.
    """

    return (np.matmul(m_a, m_b))
