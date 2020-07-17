#!/usr/bin/env python3


def matrix_shape(mat):
    """determines the shape of the given matrix"""
    matShape = []
    pres = True
    curMat = mat
    while type(curMat) == list:
        matShape.append(len(curMat))
        curMat = curMat[0]
    return matShape
