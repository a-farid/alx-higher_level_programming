#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        tupleA = (0, 0)
    elif len(tuple_a) == 1:
        tupleA = (tuple_a[0], 0)
    else:
        tupleA = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tupleB = (0, 0)
    elif len(tuple_b) == 1:
        tupleB = (tuple_b[0], 0)
    else:
        tupleB = (tuple_b[0], tuple_b[1])

    valueA = tupleA[0] + tupleB[0]
    valueB = tupleA[1] + tupleB[1]
    return (valueA, valueB)
