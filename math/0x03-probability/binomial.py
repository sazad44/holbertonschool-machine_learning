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
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = 0
            for d in data:
                variance += (mean - d) ** 2
            variance = variance / len(data)
            self.p = float(1 - (variance / mean))
            self.n = int(round(mean / self.p))
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculate pmf of binomial given k successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        nFac = 1
        kFac = 1
        nMkFac = 1
        for i in range(1, self.n + 1):
            nFac *= i
        for i in range(1, k + 1):
            kFac *= i
        for i in range(1, self.n - k + 1):
            nMkFac *= i
        return (
            nFac / (
                kFac * nMkFac
            )
        ) * (
            self.p ** k
        ) * (
            (
                1 - self.p
            ) ** (
                self.n - k
            )
        )

    def cdf(self, k):
        """calculates cdf value based on k successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdfValue = 0
        for i in range(k + 1):
            cdfValue += self.pmf(i)
        return cdfValue
