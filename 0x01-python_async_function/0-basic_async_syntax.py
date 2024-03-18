#!/usr/bin/env python3
"""basic async module"""

import asyncio
import random


async def wait_random(max_delay=10):
    """wait_random
    Args:
        max_delay: the delay
    Returns:
        the delay
    """
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)
    return delay
