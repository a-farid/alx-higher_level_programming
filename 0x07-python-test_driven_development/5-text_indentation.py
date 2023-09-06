#!/usr/bin/python3
""" This module having a function  that prints a text
with 2 new lines after each of these characters: . ? : """


def text_indentation(text):
    """ Function that prints a text with 2 new lines
    after each of these characters: . ? : 

    Args:
        text: the test to convert.

    Returns:
        A text with multiple lines if they are the characters . ? :

    Raises:
        TypeError: size must be an integer

    """
    # Check if the text is string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt = text[:]

    for d in ".?:":
        list_txt = txt.split(d)
        txt = ""
        for i in list_txt:
            i = i.strip(" ")
            txt = i + d if txt is "" else txt + "\n\n" + i + d

    print(txt[:-3], end="")
