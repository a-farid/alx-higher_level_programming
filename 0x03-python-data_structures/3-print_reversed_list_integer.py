#!/usr/bin/python3

"""
    a function that replaces an element of a list at a specific position

    Args:
        my_list: list
        
    return:
        list reversed
"""


def print_reversed_list_integer(my_list=[]):
    listRev = []
    for i in range(len(my_list)):
        listRev.insert(0, my_list[i])
    for i in range(len(listRev)):
        print(listRev[i])
