#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listRev = []
    if my_list:
        for i in range(len(my_list)):
            listRev.insert(0, my_list[i])
        for i in range(len(listRev)):
            print('{:d}'.format(listRev[i]))
