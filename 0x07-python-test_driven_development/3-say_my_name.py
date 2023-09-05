#!/usr/bin/python3
"""This module having a function that prints full name"""


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>.

    Args:
        first_name: First name.
        last_name: Last name (optional).

    Returns:
        The string My name + the full name

    Raises:
        TypeError: first_name and last_name must be a string

    """
    # Check if the first_name is string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if the last_name is string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
