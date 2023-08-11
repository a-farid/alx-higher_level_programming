#!/usr/bin/python3

"""
    Get an element from a list

    Args:
        my_list: list
        idx: Index of element

    return:
        Element from list
"""


def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return None
    return "{}".format(my_list[idx])
