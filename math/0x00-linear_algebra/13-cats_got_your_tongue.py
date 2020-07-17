#!/usr/bin/env python3
"""task 13 function to concatenate two given matrices"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates two given matrices along axis"""
    return np.concatenate((mat1, mat2), axis)
