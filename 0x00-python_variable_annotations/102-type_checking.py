#!/usr/bin/env python3
"""
    Create a new list by repeating each element
"""
from typing import Tuple, Optional, List


def zoom_array(lst: Tuple, factor: Optional[int] = 2) -> List[int]:
    """
        Create a new list by repeating each element.
    """
    if factor is None:
        factor = 2
    return [i for i in lst for _ in range(factor)]


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
