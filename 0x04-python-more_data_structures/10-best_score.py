#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    best_score = 0
    best_key = ''
    for key in a_dictionary:
        if a_dictionary[key] >= best_score:
            best_score = a_dictionary[key]
            best_key = key
    return best_key
