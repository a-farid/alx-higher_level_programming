#!/usr/bin/python3
"""A function defined to convert object to JSON representation"""
import json


def to_json_string(my_obj):
    """Convert Object to JSON representation

    Args:
        my_obj: The object to convert.
    Returns:
        A JSON representation.
    """
    return json.dumps(my_obj)
