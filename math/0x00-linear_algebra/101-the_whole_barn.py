#!/usr/bin/env python3
"""task 16 function to add matrices of the same shape"""


def add_matrices(mat1, mat2):
    """add matrices of the same shape"""
    if len(mat1) != len(mat2) or type(mat1[0]) != type(mat2[0]):
        return None
    newMat = []
    for mat in range(len(mat1)):
        if type(mat1[mat]) == list:
            newMat.append(add_matrices(mat1[mat], mat2[mat]))
        else:
            newMat.append(mat1[mat] + mat2[mat])
    if None in newMat:
        return None
    return newMat
