#!/usr/bin/env python3
"""
a simple redis file
"""

import redis
import datetime

r = redis.Redis()
r.mset({
    'croatia': 'zagreb',
    'bahamas': 'nassau'
    })

# print(r.get('bahamas'))


stoday = today.isoformat()
print(istoday)

r.sadd(stoday, *visitors)

r.smembers(stoday)

r.scard(today.isoformat())
