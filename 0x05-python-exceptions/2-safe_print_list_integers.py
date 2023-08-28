#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print('X is', x)
    res = list(filter(lambda x: type(x) == int, my_list))
    leng = 0
    try:
        for i in range(x):
            print(res[i], end='')
            leng += 1
        print()
        return int(leng)
    except IndexError:
        return "Index out of range"
