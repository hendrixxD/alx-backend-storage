#!/usr/bin/env python3

import redis
import json
from cryptography.fernet import Fernet

r = redis.Redis()

cipher = Fernet(Fernet.generate_key())
info = {
        "cardnum": 2211849528391929,
        "exp": [2020, 9],
        "cv2": 842,
}

r.set("user: 1000",
        cipher.encrypt(json.dumps(info).encode('utf-8')))

enkrypt_key = r.get('user:1000')
print(enkrypt_key)

# decrypt
print(cipher.decrypt(r.get('user: 1000')))

# load in json
print(json.loads(cipher.decrypt(r.get('user: 1000'))))
