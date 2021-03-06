#!/usr/bin/env python3
"""Poisson Class to represent poisson distribution"""


class Poisson():
    """Representation of Poisson Distribution"""
    def __init__(self, data=None, lambtha=1.):
        """initialization function for class"""
        self.e = 2.7182818285
        self.pi = 3.1415926536
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """calculates value of PMF for given successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        denom = 1
        for i in range(k, 1, -1):
            denom *= i
        pmfValue = ((self.e**(-self.lambtha))*(self.lambtha**k)) / denom
        return pmfValue

    def cdf(self, k):
        """calculates value f CDF for given no of successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdfValue = 0
        for i in range(k + 1):
            cdfValue += self.pmf(i)
        return cdfValue
