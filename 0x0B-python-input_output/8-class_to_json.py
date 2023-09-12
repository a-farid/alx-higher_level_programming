#!/usr/bin/python3
"""A function defined to return a Python class-to-JSON ."""


def class_to_json(obj):
    """Return the dictionary of a simple data struct"""
    return obj.__dict__
