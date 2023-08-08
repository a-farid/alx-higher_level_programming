#!/usr/bin/python3
def remove_char_at(str, n):
    rm = ""
    for i in range(len(str)):
        if i != n:
            rm = rm + str[i]
    return (rm)
