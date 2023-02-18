#!/usr/bin/python3

import requests as req
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        res = requests.get(url)

        # if response is successfull, no excetion
        res.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'other erro occurred: {err}')
    else:
        print('Success!')
