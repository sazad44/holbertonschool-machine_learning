#!/usr/bin/env python3
"""Normal distribution class"""


class Normal():
    """class to represent Normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """initialization function for class"""
        self.e = 2.7182818285
        self.pi = 3.141592653
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sumOfDiffS = 0
            for d in data:
                sumOfDiffS += (d - self.mean) ** 2
            self.stddev = (sumOfDiffS / len(data)) ** (1/2)

    def z_score(self, x):
        """calculates z-score of given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calculates x-value of given z-score"""
        return self.mean + self.stddev * z

    def pdf(self, x):
        """calculates pdf of distribution based on x-value"""
        return (
            self.e ** (
                -(
                    (
                        x - self.mean
                    ) ** 2
                ) / (
                    2 * (
                        self.stddev ** 2
                    )
                )
            )
        ) / (
            self.stddev * (
                (
                    2 * self.pi
                ) ** .5
            )
        )
