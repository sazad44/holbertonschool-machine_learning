#!/usr/bin/env python3
"""task 7 py function to concatenate matrices along axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a certain axis"""
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    elif axis == 1 and len(mat1) != len(mat2):
        return None
    elif axis > 1:
        return None
    else:
        newMat = []
        if axis == 0:
            for r in mat1:
                newMat.append(r.copy())
            for r in mat2:
                newMat.append(r.copy())
        elif axis == 1:
            for r in range(len(mat1)):
                newMat.append([])
                for c in mat1[r]:
                    newMat[r].append(c)
                for c in mat2[r]:
                    newMat[r].append(c)
    return newMat
