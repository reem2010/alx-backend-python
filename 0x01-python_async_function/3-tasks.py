#!/usr/bin/env python3
"""async module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """task_wait_random
    Args:
        max_delay: the delay
    Returns:
        task
    """
    return asyncio.create_task(wait_random(max_delay))
