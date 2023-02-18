#!/usr/bin/env python3
"""
implementing an expiring web cache and tracker
"""

import redis
import requests

def get_page(url: str) -> str:
    """
    args:
        url: str
    return -> 
    """

