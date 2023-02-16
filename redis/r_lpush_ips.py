#!/usr/bin/env python3
"""
"""

import datetime
import ipaddress

import redis

# where all bad eggs IP address are placed.
blacklist =  set()
MAXVISITS = 15

ipwatcher = redis.Redis(db=5)

while True:
    _, addr = ipwatcher.blpop('ips')
    addr = ipaddress.ip_address(addr.decode('utf-8'))
    
    now = datetime.datetime.utcnow()
    addrts = f'{addr}: {now.minute}'
    n = ipwatcher.incrby(addrts, 1)
    
    if n >= MAXVISITS:
        print(f"Hat bot detected!: {addr}")
        blacklist.add(addr)
    else:
        print(f"{now}:  saw {addr}")

    _ = ipwatcher.expire(addrts, 60)

for _ in range(20):
    r.lpush('ips', '104.174.118.18')

print(r.lastsave())
