# /GET/

## Content

the response of a GET request has some valuable info know as payload in the message body.

To see the response’s content in bytes, you use .content:
- >>> res = requests.get('https://api.github.com')
- >>> res.content()

in a string format
- >>> res.text()

specifying the type of encoding to be used
- >>> res.encoding = 'utf-8'

in json()
- >>> res.json()
