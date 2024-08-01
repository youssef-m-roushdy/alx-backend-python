#!/usr/bin/env python3
"""
    Floor a float number to the nearest lower integer.
"""


def floor(n: float) -> int:
    """
    Floor a float number to the nearest lower integer.

    Parameters:
    n (float): The number to floor.

    Returns:
    int: The floored integer value of n.
    """
    if n < 0 and n != int(n):
        return int(n) - 1
    return int(n)
