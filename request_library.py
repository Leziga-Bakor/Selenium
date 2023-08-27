import requests
''''
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


# status code
response = requests.get('https://httpbin.org/status/500')

if response.status_code == requests.codes.not_found:
    print("Not Found")

else: 
    print(response.status_code)



headers = {
    'User-Agent': 'HelloWorld/1.1'
}

response = requests.get('https://httpbin.org/user-agent', headers=headers)

print(response.text)

'''

headers = {
    'Accept': 'image/jpeg'
}

response = requests.get('https://httpbin.org/image', headers=headers)

with open("myimage.jpg", 'wb') as f:
    f.write(response.content)