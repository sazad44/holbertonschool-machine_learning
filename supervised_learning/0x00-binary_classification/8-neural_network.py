#!/usr/bin/env python3
"""Class definitions for neural network with 1 hidden layer"""
import numpy as np


class NeuralNetwork():
    """Neural network class definition"""
    def __init__(self, nx, nodes):
        """initialization func for class"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        elif nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.array([float(0)] * nodes).reshape(nodes, 1)
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
