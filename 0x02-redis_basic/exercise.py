#!/usr/bin/env python3
"""
writing strings to redis
"""
import functools
import redis
from typing import Union, Optional, Callable
from redis.typing import Union
import uuid


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

    @staticmethod
    def count_calls(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(self, *args, **kwargs):
            key = fn.__qualname__
            self._calls.incr(key)
            return fn(self, *args, **kwargs)
        return wrapped

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
