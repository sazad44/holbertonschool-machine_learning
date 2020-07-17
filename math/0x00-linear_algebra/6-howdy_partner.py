#!/usr/bin/env python3
"""task 6 concatenate two arrays"""


def cat_arrays(arr1, arr2):
    """concatenate two arrays"""
    newArr = []
    for i in arr1:
        newArr.append(i)
    for i in arr2:
        newArr.append(i)
    return newArr
