#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    class Cache
    """
    def __init__(self):
        """
        init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
