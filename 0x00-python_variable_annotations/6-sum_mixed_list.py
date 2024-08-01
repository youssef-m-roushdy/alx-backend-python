#!/usr/bin/env python3
"""
    Calculate the sum of a list containing integers and float numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and float numbers.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and float numbers to sum.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
