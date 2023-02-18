#!/usr/bin/env python3
"""
Headers
"""

import requests as req

res = req.get('https://api.github.com/user')

# print(res.headers)

print(res.headers['Content-Type'])
