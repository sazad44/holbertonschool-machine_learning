#!/usr/bin/env python3
"""task 3 python script to transpose a matrix"""


def matrix_transpose(mat):
    """transpose given matrix assume never empty"""
    newMat = []
    col = len(mat[0])
    for i in range(col):
        newMat.append([])
        for r in mat:
            newMat[i].append(r[i])
    return newMat
