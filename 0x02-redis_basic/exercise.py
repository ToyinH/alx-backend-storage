#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, None]:
        """
        get method
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        get_str method
        """
        return self.get(
            key, fn=lambda d: d.decode("utf-8") if d is not None else None
                        )

    def get_int(self, key: str) -> Union[int, None]:
        """
        get_int method
        """
        return self.get(key, fn=lambda d: int(d) if d is not None else None)
