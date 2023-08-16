#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = set({})
    for i in set_1:
        result.add(i) if i in set_2 else None
    return result
