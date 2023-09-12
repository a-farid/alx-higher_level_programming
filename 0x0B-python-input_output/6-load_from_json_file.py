#!/usr/bin/python3
"""A function defined to a JSON file-reading"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
