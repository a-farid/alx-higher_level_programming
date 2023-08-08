#!/usr/bin/python3
for c in range(97, 123):
    letter = "{:c}".format(c)
    if letter != 'e' and letter != 'q':
        print("{}".format(letter), end='')
