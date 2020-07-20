#!/usr/bin/env python3
"""task 17 py function to concatenate matrices based on axis"""


def cat_matrices(mat1, mat2, axis=0):
    """py functin to concatenate matrices on a specified axis"""
    if (axis % 2) and len(mat1) != len(mat2):
        return None
    curMat1 = mat1
    curMat2 = mat2
    while not isinstance(curMat1, int):
        if isinstance(curMat1[0], int) and len(curMat1) != len(curMat2):
            if axis % 2 == 0:
                return None
        elif isinstance(curMat1[0], list) and isinstance(curMat1[0][0], int):
            if len(curMat1) != len(curMat2) and axis % 2 != 0:
                return None
        elif not isinstance(curMat2[0], type(curMat1[0])):
            return None
        curMat1 = curMat1[0]
        curMat2 = curMat2[0]
    newMat = []
    if axis > 0:
        for i in range(len(mat1)):
            newMat.append(cat_matrices(mat1[i], mat2[i], axis - 1))
    else:
        for n in mat1:
            newMat.append(n)
        for n in mat2:
            newMat.append(n)
    if None in newMat:
        return None
    return newMat
