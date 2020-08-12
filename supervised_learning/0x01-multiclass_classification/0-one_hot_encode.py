#!/usr/bin/env python3
"""func to encode vector into one hot matrix"""
import numpy as np


def one_hot_encode(Y, classes):
    """encodes label vector to one hot matrix"""
    try:
        oh = np.zeros((classes, Y.max()+1))
        oh[Y, np.arange(Y.size)] = 1
        return oh
    except:
        return None
