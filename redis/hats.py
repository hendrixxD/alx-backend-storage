#!/usr/bin/env python3
"""
limiited edition hats
"""
import redis
import random


random.seed(444)

hats = {f'hat: {random.getrandbits(32)}': i for i in (
    {
        'color': 'black',
        'price': 49.99,
        'style': 'fitted',
        'quantity': 1000,
        'npurchased': 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

r = redis.Redis(db=1)

with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hset(h_id, hat)
    pipe.execute()

r.bgsave()

print(r.hgetall('hat:56854717'))

r.keys()

# if items in stock and it is purchased, increase quantity by -1
r.hincrby("hat:56854717", 'quantity', -1)

# to confirm that the quantity has been reduced after purchase
r.hget('hat:56854717', 'quantity')

# adding item to npurchase increas by 1
r.hincrby('hat: 56854717', 'npurchased', 1)
