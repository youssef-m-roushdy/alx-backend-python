#!/usr/bin/env python3
"""
This module defines an asynchronous generator.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates 10 random numbers between 0 and 10,
    with a 1-second delay between each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
