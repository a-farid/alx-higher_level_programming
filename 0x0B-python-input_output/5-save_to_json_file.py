#!/usr/bin/python3
"""A function defined to a JSON file-writing"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
