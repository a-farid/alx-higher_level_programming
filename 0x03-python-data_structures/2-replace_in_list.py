#!/usr/bin/python3

"""
    Function that replaces an element of a list at a specific position

    Args:
        my_list: list
        idx: Index of element
        element: element to replace with

    return:
        list replaces
"""


def replace_in_list(my_list, idx, element):
    if (idx < 0):
        return None
    if (idx > len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
