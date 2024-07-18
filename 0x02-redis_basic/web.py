#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data and tracks access counts.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function for caching the output and tracking access.
        '''
        # Increment the access count
        redis_store.incr(f'count:{url}')

        # Check if the result is already cached
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')

        # Fetch the page content and handle exceptions
        try:
            result = method(url)
            # Cache the result with an expiration time of 10 seconds
            redis_store.setex(f'result:{url}', 10, result)
            return result
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return ""

    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses
    return response.text


if __name__ == "__main__":
    import time

    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"

    # Fetch the page and print content
    print(get_page(test_url))

    # Sleep for 2 seconds and fetch again to test caching
    time.sleep(2)
    print(get_page(test_url))

    # Sleep for 12 seconds to test cache expiry
    time.sleep(12)
    print(get_page(test_url))
