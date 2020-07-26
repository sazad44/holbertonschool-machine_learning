#!/usr/bin/env python3
"""task 17 py function to integrate a polynomial"""


def poly_integral(poly, C=0):
    """py function to calculate integral of poly"""
    if not isinstance(
            poly,
            list
    ) or not isinstance(
        C, (
            float,
            int
        )
    ):
        return None
    newPoly = [C]
    for c in range(len(poly)):
        appVal = poly[c] / (c + 1)
        if appVal.is_integer():
            newPoly.append(int(appVal))
        else:
            newPoly.append(appVal)
    if newPoly[:-1] == 0:
        newPoly = newPoly[:-1]
    return newPoly