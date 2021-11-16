## API KEY: hidden in config.py, not published to git
## SAMPLE URL REQUEST: https://api.nasa.gov/planetary/apod?api_key=Ga7t4uEhzVS1WoLmVHDcZrBZXFA5RD61rtwv1S4s
## ACCOUNT EMAIL: kevinlowen@gmail.com
## ACCOUNT ID: hidden in config.py, not published to git

from PIL import Image
import requests
import config

r               = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + config.API_KEY)
author          = r.json()['copyright']
date            = r.json()['date']
explanation     = r.json()['explanation']
hdurl           = r.json()['hdurl']
media_type      = r.json()['media_type']
title           = r.json()['title']
url             = r.json()['url']

# print('author is      : ' + author        )
# print('date is        : ' + date          )  
# print('explanation is : ' + explanation   )
# print('hdurl is       : ' + hdurl         )
# print('media_type is  : ' + media_type    )
# print('title is       : ' + title         )
# print('url is         : ' + url           )

img = Image.open(requests.get(url, stream=True).raw)
#img.show()