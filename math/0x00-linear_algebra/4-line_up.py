#!/usr/bin/env python3
"""task 4 function to add arrays"""


def add_arrays(arr1, arr2):
    """add arrays of the same shape"""
    if len(arr1) != len(arr2):
        return None
    newArr = []
    for i in range(len(arr1)):
        newArr.append(arr1[i] + arr2[i])
    return newArr
