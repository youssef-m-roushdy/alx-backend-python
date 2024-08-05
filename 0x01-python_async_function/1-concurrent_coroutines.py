#!/usr/bin/env python3
"""
    This module defines the wait_n function.
"""

import heapq
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        Executes wait_random multiple times and returns the results.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    heap = []

    for task in asyncio.as_completed(tasks):
        result = await task
        heapq.heappush(heap, result)

    while heap:
        results.append(heapq.heappop(heap))

    return results
