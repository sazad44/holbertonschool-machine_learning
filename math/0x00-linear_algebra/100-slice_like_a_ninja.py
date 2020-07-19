#!/usr/bin/env python3
"""function to slice matrix by axes"""


def np_slice(matrix, axes={}):
    """functions slices matrix by axes and slice provided in axes"""
    curMat = matrix
    newMat = []
    sliceParams = ()
    for axis in range(max(axes.keys()) + 1):
        if axis in axes.keys():
            if len(axes[axis]) == 1:
                sliceParams += (slice(axes[axis][0]),)
                continue
            sliceGroup = [None, None, None]
            for s in range(len(axes[axis])):
                sliceGroup[s] = axes[axis][s]
            start, stop, step = tuple(sliceGroup)
            sliceParams += (slice(start, stop, step),)
        else:
            sliceParams += (slice(None, len(curMat), None),)
        curMat = curMat[0]
    newMat = matrix[sliceParams]
    return newMat
