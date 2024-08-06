#!/usr/bin/env python3
"""
This module defines a function to measure the runtime of async_comprehension.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time it takes to execute async_comprehension.

    Returns:
        float: The time in seconds that it took to execute async_comprehension.
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension())
    t = time.perf_counter() - s
    return t
