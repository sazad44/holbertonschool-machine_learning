#!/usr/bin/env python3
"""task 12 py function to perform arithmetic operations on matrices"""


def np_elementwise(mat1, mat2):
    """add, subtract, muliply, divide given matrices"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
