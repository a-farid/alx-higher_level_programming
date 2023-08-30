#!/usr/bin/python3

'''Check if the value is Integer and print it if true'''

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
    