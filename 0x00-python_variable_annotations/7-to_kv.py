#!/usr/bin/env python3
"""Type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """Returns tuple of a string and a float"""
    return (k, v ** 2)
