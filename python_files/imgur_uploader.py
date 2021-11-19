from base64 import b64encode
import json
import requests
import config



client_id = config.IMGUR_CLIENT_ID
# headers = ['Authorization'] = f'Client-ID {client_id}'
headers = {"Authorization": f'Client-ID {client_id}'}
api_key = config.IMGUR_CLIENT_SECRET
url = "https://api.imgur.com/3/upload.json"


# print(r'..\media\test.jpg')

j1 = requests.post(
    url, 
    headers = headers,
    data = {
        'key': api_key, 
        #'image': b64encode(open(r'..\media\test.jpg', 'rb').read()),
        'image': open(r'..\media\test.jpg', 'rb').read(),
        'type': 'base64',
        'name': 'test.jpg',
        'title': 'Picture no. 1'
    }
)

