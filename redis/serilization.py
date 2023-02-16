restaurant_484272 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}

# this isnt possible using the convemtional way
# there are two ways to do this:
# 1. serialize the values into a string

import json

import redis

from pprint import pprint

r = redis.Redis()
print(r.set(484272, json.dumps(restaurant_484272)))

# converting back, deserializin
pprint(json.loads(r.get(484272)))

#also using yaml
# python -m pip isntall PyYAML
import yaml

yaml.dump(restaurant_484272)

# option 2. use a delimiter in key strings

