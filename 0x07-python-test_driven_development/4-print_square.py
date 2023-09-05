#!/usr/bin/python3
"""This module having a function that prints a square with #"""


def print_square(size):
    """ Function that prints a square.

    Args:
        size: the size of the square.

    Returns:
        A square with the charater #

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    """
    # Check if the size is integer
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    # Check if the size is less then
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print()
