#!/usr/bin/env python3
"""Exponential distribution class"""


class Exponential():
    """class to represent Exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        """initialization func for class"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = len(data) / sum(data)
