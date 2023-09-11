#!/usr/bin/python3

'''Module including a class MyList that inherits from list '''


class MyList(list):
    """A class inherits from list class"""

    def print_sorted(self):
        '''A function that prints the list sorted (ascending sort)'''

        sorted_list = sorted(self)  # Create a new sorted list
        print(sorted_list)
