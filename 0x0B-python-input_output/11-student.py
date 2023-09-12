#!/usr/bin/python3
"""A class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """ Replace all attributes of the student """
        for m, v in json.items():
            setattr(self, m, v)
