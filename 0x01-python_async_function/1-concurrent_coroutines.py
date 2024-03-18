#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


"""
- import wait_random from the previous python file that you’ve,
written and write an async routine
- called wait_n that takes in 2 int arguments (in this order): n and max_delay
-  You will spawn wait_random n times with the specified max_delay
- wait_n should return the list of all the delays (float values).
- The list of the delays should be in ascending order without using sort(),
because of concurrency.
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of delays"""

    delays: List[asyncio.Future[float]] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))

    result: List[float] = []
    for delay in asyncio.as_completed(delays):
        result.append(await delay)
    return result
