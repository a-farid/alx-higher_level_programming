#!/usr/bin/python3
"""A function defined to a file-appending"""


def append_write(filename="", text=""):
    """Append a string to a text file.

    Args:
        filename: The name of the file to write
        text: The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

