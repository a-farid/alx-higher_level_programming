#!/usr/bin/python3
'''
 Module contains a function that returns True if the object is an
 instance of a class that  inherited (directly or indirectly)
 from the specified class ; otherwise False
'''


def inherits_from(obj, a_class):
    """function that checks if obj is inherists of a class

    Args:
        obj: The object to check with
        a_class: The class to check
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
