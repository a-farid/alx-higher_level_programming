#!/usr/bin/python3
"""A function defined to convert JSON representation to object"""
import json


def from_json_string(my_str):
    """Convert JSON representation to str

    Args:
        my_str: The JSON to convert.
    Returns:
        Am object representation.
    """
    return json.loads(my_str)
