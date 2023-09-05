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
    res = text.strip(' ')
    res = '.'.join(list(map(lambda x: x.strip(), res.split('.'))))
    res = '?'.join(list(map(lambda x: x.strip(), res.split('?'))))
    res = ':'.join(list(map(lambda x: x.strip(), res.split(':'))))
    res = res.replace('.', '.@').replace('?', '?@')
    res = res.replace(':', ':@').replace('@', '\n\n')

    print(res)
