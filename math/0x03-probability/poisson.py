#!/usr/bin/env python3
"""Poisson Class to represent poisson distribution"""


class Poisson():
    """Representation of Poisson Distribution"""
    def __init__(self, data=None, lambtha=1.):
        """initialization function for class"""
        if data is None:
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise ValueError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
