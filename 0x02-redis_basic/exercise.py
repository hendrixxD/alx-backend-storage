#!/usr/bin/env python3
"""
writing strings to redis
"""
from functools import wraps
import redis
from typing import Union, Optional, Callable
# from redis.typing import Union
import uuid


def count_calls(method: Callable) -> Callable:
    """
    count function calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    function call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    function to display the history of
    calls of a particular function
    """
    key = method.__qualname__
    redis_cache = redis.Redis()
    input_key = key + ":inputs"
    output_key = key + ":outputs"

    inputs = redis_cache.lrange(input_key, 0, -1)
    outputs = redis_cache.lrange(output_key, 0, -1)

    calls = redis_cache.get(key).decode('utf-8')
    print("{} was called {} times:".format(key, calls))

    for i, o in zip(inputs, outputs):
        i = i.decode('utf-8')
        o = o.decode('utf-8')

        print("{}(*{}) -> {}".format(key, i, o))


class Cache:
    """
    class Cache
    """
    def __init__(self):
        """
        redis: a private attribute
        """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)

        # flush instance
        self._redis.flushdb

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        data: returns a union of data types
        return -> string
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: callable = None) -> \
            Union[str, bytes, int, float]:
        """ key: str
            fn : callable
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with correct conversion function"""
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with correct conversion function"""

        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except ValueError:
            return value
