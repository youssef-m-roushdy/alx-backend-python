#!/usr/bin/env python3
"""
    Create a multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies its input by
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
