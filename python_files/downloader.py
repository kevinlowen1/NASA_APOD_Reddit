import requests
import config
import urllib
# from pytube import YouTube

def nasa_apod_downloader():
    # r               = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + config.NASA_API_KEY + '&date=2021-11-10')
    r               = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + config.NASA_API_KEY)
    # print(r.json())
    #author          = r.json()['copyright']
    date            = r.json()['date']
    explanation     = r.json()['explanation']
    # hdurl           = r.json()['hdurl']
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

    if(media_type == 'video'):
        print('video APOD, wtf dude')
        file_location = youtubeDownloader()
    else:
        print('continuing as normal, photo APOD')
        file_location = urllib.request.urlretrieve(url, r'C:\temp\test.jpg')
    
    info = [title, url, explanation,  date, media_type, file_location]
    return info

def youtubeDownloader():
    # yt = "https://www.youtube.com/embed/25FfQ9MEQE8"
    print("stuff to happen here, in youtubeDownloader, later")
    return "nothing to return"

if __name__ == "__main__":
   nasa_apod_downloader()