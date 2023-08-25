import requests

# Get

params = {
    'name':'Mike',
    'age': 25
}

respons = requests.get('https://httpbin.org/get', params = params)

res_json = respons.json()

del res_json['origin']

print(res_json)


# Post

payload = {
    'name': 'charles',
    'age': 30
}

respons = requests.post('https://httpbin.org/post', data = payload)

res_json = respons.json()

del res_json['origin']

print(res_json)