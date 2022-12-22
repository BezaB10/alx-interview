#!/usr/bin/python3
"""
    0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    t_row = [1]
    temp_l = [0]
    pT = []

    if n <= 0:
        return pT

    for i in range(n):
        pT.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return pT
