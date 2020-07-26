#!/usr/bin/env python3
"""task 9 py script to code summation function"""


def summation_i_squared(n):
    """calculates summ of i(squared) from 1 to n"""
    if not isinstance(n, (int, float)):
        return None
    return int(n * (n + 1) * (2 * n + 1) / 6)
