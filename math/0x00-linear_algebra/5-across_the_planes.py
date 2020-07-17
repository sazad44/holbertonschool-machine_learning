#!/usr/bin/env python3
"""task 5 function to add matrices"""


def add_matrices2D(mat1, mat2):
    """add 2D matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    sumMat = []
    for r in range(len(mat1)):
        sumMat.append([])
        for c in range(len(mat1[r])):
            sumMat[r].append(mat1[r][c] + mat2[r][c])
    return sumMat
