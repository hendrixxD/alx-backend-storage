#!/usr/bin/env python3
"""
"""
# r = __import__('').r
import redis
from datetime import timedelta

r = redis.Redis()

# setex: "SET" with expiration
time = r.setex(
        "runner",
        timedelta(minutes=1),
        value='now you see me, now you dont')
print(time)

# time to live in seconds
print(r.ttl('runner'))

# time to leave in milliseconds
print(r.pttl('runner'))

# not expired yet
print(r.get('runner'))

# set new expire window
r.expire('runner', timedelta(seconds=3))

r.get('runner')

# key & and value are both gone
r.exists('runner')
