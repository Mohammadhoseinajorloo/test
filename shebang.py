#!/usr/bin/env python3


def debugger(a):
    # set a trace for debugging
    result = [a[element] for element in range(0, len(a))]
    return result


print(debugger([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
