#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if (b != 0):
            print('Inside result: {:.1f}'.format(a / b))
        else: 
            print('Inside result: None')

    except ZeroDivisionError:
        return None
    finally:
        if (b != 0):
            return a / b
        else:
            return None
