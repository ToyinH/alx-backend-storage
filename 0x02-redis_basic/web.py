#!/usr/bin/env python3

import requests
import time
from functools import wraps

def cache_with_count(expiration_time=10):
    cache = {}

    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Check if URL is in cache and not expired
            if url in cache and time.time() - cache[url]['timestamp'] < expiration_time:
                cache[url]['count'] += 1
                return cache[url]['content']

            # If not in cache or expired, fetch the content
            content = func(url)

            # Update cache
            cache[url] = {'content': content, 'timestamp': time.time(), 'count': 1}
            return content
        return wrapper
    return decorator

@cache_with_count()
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
