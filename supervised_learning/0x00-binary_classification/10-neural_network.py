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
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.array([float(0)] * nodes).reshape(nodes, 1)
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """getter func for W1"""
        return self.__W1

    @property
    def b1(self):
        """getter func for b1"""
        return self.__b1

    @property
    def A1(self):
        """getter func for A1"""
        return self.__A1

    @property
    def W2(self):
        """getter func for W2"""
        return self.__W2

    @property
    def b2(self):
        """getter func for b2"""
        return self.__b2

    @property
    def A2(self):
        """getter func for A2"""
        return self.__A2

    def forward_prop(self, X):
        """calculates forward propagation of neural network"""
        matmul = np.matmul(self.__W1, X)
        actVals = 1 / (1 + np.exp(-(matmul + self.__b1)))
        self.__A1 = actVals
        matmul = np.matmul(self.__W2, self.__A1)
        actVals = 1 / (1 + np.exp(-(matmul + self.__b2)))
        self.__A2 = actVals
        return self.__A1, self.__A2
