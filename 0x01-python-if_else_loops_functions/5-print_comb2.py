#!/usr/bin/python3
for c in range(00, 100):
    if c < 10:
        print("0{}".format(c), end=', ')
    elif c == 99:
        print("{}".format(c))
    else:
        print("{}".format(c), end=', ')

