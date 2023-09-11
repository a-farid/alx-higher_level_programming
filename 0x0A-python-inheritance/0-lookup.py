#!/usr/bin/python3

'''Module for creating that returns the
list of available attributes and methods of an object '''


def lookup(obj):
    '''Function that returns list of attributes and methods of an object '''
    return dir(obj)
