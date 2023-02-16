#!/usr/bin/env python3
"""
writing strings to redis
"""

import redis
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
        self._redis = redis.Redis()

        # flush instance
        self._redis.flushdb

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
        """return args key"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """args: key"""
        return self.get(key, int)
