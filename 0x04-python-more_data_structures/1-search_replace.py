#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for i in my_list:
        newList.append(replace) if search == i else newList.append(i)
    return newList
