#!/usr/bin/python3
'''Module including a class MyList that inherits from list '''


class MyList(list):
    """A class inherits from list class"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        '''A function that prints the list sorted (ascending sort)'''
        print(sorted(self))
