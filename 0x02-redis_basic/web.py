#!/usr/bin/env python3
"""
implementing an expiring web cache and tracker
"""

from functools import wraps
import redis
import requests as req
from typing import Callable

rds = redis.Redis()
"""redis client"""


def count_requests(method: Callable) -> Callable:
    """ Decortator for counting how many times a request
    has been made """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        rds.incr(f"count:{url}")
        cached_html = rds.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rds.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    args:
        url: str
    return ->
    """

    res = req.get(url)

    return res.text
