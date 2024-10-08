#!/usr/bin/env python3
"""
    Calculate the sum of a list of float numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Parameters:
    input_list (List[float]): The list of float numbers to sum.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(input_list)
