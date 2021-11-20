from imgurpython import ImgurClient
import config

client = ImgurClient(config.IMGUR_CLIENT_ID, config.IMGUR_CLIENT_SECRET)
items = client.gallery()

for item in items:
    print(item.link)
    print(item.title)
    print(item.views)