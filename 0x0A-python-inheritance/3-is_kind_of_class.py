#!/usr/bin/python3
'''
Module including a function that returns True if the object is an
instance of, or if the object is an instance of a class that
inherited from, the specified class ; otherwise False
'''


def is_kind_of_class(obj, a_class):
    """function that checks if onj is instance of a class

    Args:
        obj: The object to check with
        a_class: The class to check
    Returns:
        True: if obj is instance of a_class
        False: Otherwise
    """
    return isinstance(obj, a_class)
