#!/usr/bin/env python3
"""task 17 py function to integrate a polynomial"""


def poly_integral(poly, C=0):
    """py function to calculate integral of poly"""
    if not isinstance(
            poly,
            list
    ) or len(
        poly
    ) == 0 or not isinstance(
        C,
        int
    ):
        return None
    newPoly = [C]
    for c in range(len(poly)):
        appVal = poly[c] / (c + 1)
        if appVal.is_integer():
            newPoly.append(int(appVal))
        else:
            newPoly.append(appVal)
    if sum(newPoly) == 0:
        return [0]
    cutoff = 1
    while newPoly[-cutoff] == 0:
        cutoff += 1
    if newPoly[-1] == 0:
        newPoly = newPoly[:-(cutoff - 1)]
    return newPoly
