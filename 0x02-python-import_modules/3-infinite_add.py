#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of infinit arguments"""
    import sys

    tl = 0
    for i in range(len(sys.argv) - 1):
        tl += int(sys.argv[i + 1])
    print("{}".format(tl))
