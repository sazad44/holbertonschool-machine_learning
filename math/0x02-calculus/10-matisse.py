#!/usr/bin/env python3
"""task 10 py function to evaluate the derivative of a polynomia"""


def poly_derivative(poly):
    """task 10 function to evaluate derivative of poly"""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    elif len(poly) == 1:
        return [0]
    newPoly = []
    for c in range(len(poly)):
        if c == 0:
            continue
        newPoly.append(c * poly[c])
    return newPoly
