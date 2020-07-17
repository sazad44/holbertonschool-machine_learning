#!/usr/bin/env python3
"""task 8 py function to multiply matrices"""


def mat_mul(mat1, mat2):
    """multiply two 2D matrices if possible"""
    if len(mat1[0]) != len(mat2):
        """if columns of mat1 don't match rows of mat2 return None"""
        return None
    newMat = []
    for r in range(len(mat1)):
        """for each row in mat1"""
        newMat.append([])
        for c in range(len(mat2[0])):
            """for each column in mat2"""
            newSum = 0
            for i in range(len(mat2)):
                """for each row in mat2 add up the produc"""
                newSum += mat2[i][c]*mat1[r][i]
            newMat[r].append(newSum)
    return newMat
