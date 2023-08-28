#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    res = list(map(lambda x: str(x), my_list[:x]))
    length = 0
    try:
        for i in res:
            print(i, end='')
            length += 1
        print()
        return length
    except IndexError:
        print(f'Error, {x} longer then the list')
