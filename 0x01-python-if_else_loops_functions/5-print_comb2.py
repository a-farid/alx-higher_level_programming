#!/usr/bin/python3
for c in range(00, 100):
    if c == 99:
        print("{}".format(c))
    else:
        print("{:02}".format(c), end=', ')
