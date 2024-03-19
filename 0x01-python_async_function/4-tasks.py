#!/usr/bin/env python3
"""basic async module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task_wait_n
    Args:
        n: number to spawn wait_random
        max_delay: the delay
    Returns:
        list of  delay
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    res = []

    for task in asyncio.as_completed((tasks)):
        res.append(await task)

    return res
