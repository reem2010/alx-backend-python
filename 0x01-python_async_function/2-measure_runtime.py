#!/usr/bin/env python3
"""async module"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """measure_time
    Args:
        n: number to spawn wait_random
        max_delay: the delay
    Returns:
        Measure the runtime
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
