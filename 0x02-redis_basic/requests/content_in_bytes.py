import requests

res = requests.get('https://api.github.com')

# .content goves us access to raw bytes
print(res.content)

# converting to a string char of encoding
# such as utf-8
print(res.text)

# specifying an explicit encoding
res.encoding = 'utf-8'
print(res.text)

# converting to json..
print(res.json())
