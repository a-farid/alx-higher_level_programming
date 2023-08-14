#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    result = []
    for i in range(len(my_list)):
        if i != idx:
            result.append(my_list[i])
    return result
