#!/usr/bin/env python3
"""
intro to request module
"""

import requests as req

try:

    res = req.get('https://api.github.com')
    # print(res)

    # to verify the status code retured by response
    ver_stat_code = res.status_code
    # print(ver_stat_code)

    if res.status_code == 200:
        print('Success!')
    elif res.status_code == 404:
        print('Not Found.')

except Exception as e:
    print(e)
