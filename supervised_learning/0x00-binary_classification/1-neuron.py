#!/usr/bin/env python3
"""class for Neuron"""
import numpy as np


class Neuron():
    """Neuron Class to define a single neuron performing classification"""
    def __init__(self, nx):
        """initialization function for class"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """getter func for W"""
        return self.__W

    @property
    def b(self):
        """getter func for b"""
        return self.__b

    @property
    def A(self):
        """getter func for A"""
        return self.__A
