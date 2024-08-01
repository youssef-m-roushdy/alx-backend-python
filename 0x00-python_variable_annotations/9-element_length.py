#!/usr/bin/env python3
"""
    Create a list of tuples
"""
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Create a list of tuples where each tuple contains an element from the input
    iterable and the length of that element.
    """
    return [(i, len(i)) for i in lst]
