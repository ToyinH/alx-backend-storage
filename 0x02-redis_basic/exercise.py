#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps
import time



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

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper
    @staticmethod
    def call_history(method: Callable) -> Callable:
        def wrapper(self, *args, **kwargs):
            inputs_key = "{}:inputs".format(method.__qualname__)
            outputs_key = "{}:outputs".format(method.__qualname__)
            
            # Execute the original function to retrieve the output
            output = method(self, *args, **kwargs)
            
            # Introduce a delay to ensure that data is stored in Redis
            time.sleep(1)
            
            # Append input arguments to the inputs list
            self._redis.rpush(inputs_key, str(args))
            
            # Append the output to the outputs list
            self._redis.rpush(outputs_key, output)
            
            return output
        
        return wrapper

    @count_calls
    @call_history
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

    
