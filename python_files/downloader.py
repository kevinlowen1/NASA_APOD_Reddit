import requests
import config
import urllib

def nasa_apod_downloader():
    r               = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + config.NASA_API_KEY)
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

    testfile = urllib.request.urlretrieve(url, r'C:\temp\test.jpg')



if __name__ == "__main__":
   nasa_apod_downloader()