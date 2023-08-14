#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    BoolList = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            BoolList.append(True)
        else:
            BoolList.append(False)
    return BoolList
