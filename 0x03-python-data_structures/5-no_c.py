#!/usr/bin/python3
def no_c(my_string):
    str_without_c = ''
    if my_string:
        for i in range(len(my_string)):
            if (my_string[i] != 'c' and my_string[i] != 'C'):
                str_without_c = str_without_c + my_string[i]
    return str_without_c
