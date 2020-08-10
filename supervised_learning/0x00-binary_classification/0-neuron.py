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
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
