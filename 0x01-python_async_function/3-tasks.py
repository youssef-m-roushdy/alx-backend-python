#!/usr/bin/env python3
"""
    This module defines a function to create an asyncio task for wait_random.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Creates an asyncio task that runs wait_random with the given max_delay.
    """
    async def wrapper():
        return await wait_random(max_delay)

    return asyncio.create_task(wrapper())
