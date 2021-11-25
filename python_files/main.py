from downloader import nasa_apod_downloader
from reddit_uploader import reddit_uploader

if __name__ == "__main__":
   info = nasa_apod_downloader()

   reddit_uploader(info)