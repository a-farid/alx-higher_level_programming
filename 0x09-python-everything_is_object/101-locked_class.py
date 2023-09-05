#!/usr/bin/python3
""" This module that containt a class that avoid
    dynmaically created attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
