#!/usr/bin/env python3
"""
This module defines an asynchronous comprehension function.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from an async generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
