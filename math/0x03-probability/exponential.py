#!/usr/bin/env python3
"""Exponential distribution class"""


class Exponential():
    """class to represent Exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """initialization func for class"""
        self.e = 2.7182818285
        self.pi = 3.141592653
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

    def pdf(self, x):
        """calculates pdf for a given time period"""
        if x < 0:
            return 0
        pdfValue = self.lambtha * (self.e ** (-self.lambtha * x))
        return pdfValue

    def cdf(self, x):
        """calculates value of cdf for given time period"""
        if x < 0:
            return 0
        return 1 - self.e ** (-self.lambtha * x)
