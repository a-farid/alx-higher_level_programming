#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except:
        print('Except: {}'.format(sys.exc_info()[1]), file=sys.stderr)
        return None
    else:
        return result
