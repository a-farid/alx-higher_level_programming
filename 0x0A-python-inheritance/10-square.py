#!/usr/bin/python3
"""Defines a Rectangle Square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size: The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
