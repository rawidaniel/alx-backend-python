#!/usr/bin/env python3

"""
Module 0-basic_async_syntax
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    max_delay - awit time

    Reterive a random number between 0 and max_dely after some delay
    """
    num: float = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
