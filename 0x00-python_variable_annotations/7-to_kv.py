#!/usr/bin/env python3
"""
    Create a tuple containing a string and a number (integer or float).
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    Create a tuple containing a string and a number (integer or float).

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The number (integer or float)
    to include in the tuple.

    Returns:
    Tuple[str, Union[int, float]]: A tuple with the string and number.
    """
    return (k, v)
