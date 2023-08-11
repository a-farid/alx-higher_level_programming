#!/usr/bin/python3

"""
    Print list items

    Args:
        my_list: list

    return:
        items one by one
"""


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
