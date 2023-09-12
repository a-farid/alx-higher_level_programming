#!/usr/bin/python3
"""A function defined to a file-writing"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename: The name of the file to write
        text: The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
