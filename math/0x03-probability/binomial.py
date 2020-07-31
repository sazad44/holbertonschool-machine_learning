#!/usr/bin/env python3
"""Binomial distribution Class"""


class Binomial():
    """class representation of Binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """initialization function for Binomial class"""
        self.e = 2.7182818285
        self.pi = 3.1415926536
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            self.n = int(n)
            if p < 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            self.p = mean / (len(data) / 2)
            self.n = int(mean / self.p)
            self.p = float(mean / self.n)
