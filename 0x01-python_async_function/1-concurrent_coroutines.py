#!/usr/bin/env python3
"""
    Module to wait_n
"""
import asyncio
import heapq
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Executes wait_random multiple times
        , gathers the results
        , and returns them in sorted order.
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
