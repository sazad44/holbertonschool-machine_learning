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

    def forward_prop(self, X):
        """forward propagation func for Neuron"""
        matmul = np.matmul(self.__W, X)
        actVals = 1 / (1 + np.exp(-(matmul + self.__b)))
        self.__A = actVals
        return self.__A

    def cost(self, Y, A):
        """calculates the cost of the model using logistic regression"""
        costMat = -(Y * (np.log(A)) + (1 - Y) * np.log(1.0000001 - A))
        costSum = sum(costMat[0])
        costVal = costSum / len(costMat[0])
        return costVal

    def evaluate(self, X, Y):
        """evaluates neuron's predictions"""
        A = self.forward_prop(X)
        C = self.cost(Y, A)
        return np.round(A).astype(int), C

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """calculates one pass of gradient descent on the neuron"""
        dz = (A - Y)
        dw = np.matmul(dz, X.T) / len(dz[0])
        db = np.sum(dz) / len(dz[0]
        self.__W = self.__W - alpha * dw
        self.__b = self.__b - alpha * db
