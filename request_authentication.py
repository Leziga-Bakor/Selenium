import requests

username = 'Lez'
password = '12345'
response = requests.get('http://httpbin.org/basic-auth/Lez/12345', auth = (username,password))

print(response.status_code)
print(response.json())


# Api Key

api_key = 'your_api_key'

url = 'https://api.example.com/data'
headers = {'Authorization': f'Bearer {api_key}'}

response = requests.get(url, headers=headers)

print(response.json())

# Oauth

from requests_oauthlib import OAuth2Session

client_id = 'your_client_id'
client_secret = 'your_client_secret'
token_url = 'https://api.example.com/oauth/token'

oauth = OAuth2Session(client_id, redirect_uri='https://your-redirect-uri.com')
token = oauth.fetch_token(token_url, client_secret=client_secret)

url = 'https://api.example.com/data'
response = oauth.get(url)

print(response.json())
