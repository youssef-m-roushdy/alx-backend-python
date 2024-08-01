#!/usr/bin/env python3
"""
    Create a new list by repeating each element
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        Create a new list by repeating each element.
    """
    return [i * factor for i in lst]


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
