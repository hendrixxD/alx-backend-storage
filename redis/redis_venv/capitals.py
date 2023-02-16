import redis

capitals = {}

capitals['bahamas'] = 'Nassau'
capitals.get('bahamas')

capitals.update({
    'lebanon': 'Beirut',
    'Norway': 'oslo',
    'France': 'Paris',
    })
print([capitals.get(k) for k in ('lebanon', 'Norway', 'France')])

data = {
        'realpython' : {
            'url': 'https://realpython',
            'github': 'realpython',
            'fullname': 'real python'
            }
}

print(data)
