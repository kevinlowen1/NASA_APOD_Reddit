##Run refreshToken.py to get value to enter into config.py

import config
import requests
import pandas
import praw

# ## Create variable for pandas dataframes
# df = pandas.DataFrame()

# ## Create variables for reddit connection
# auth = requests.auth.HTTPBasicAuth(config.REDDIT_OAUTH_CLIENT_ID, config.REDDIT_SECRET_KEY)
# data = {
#     'grant_type': 'password',
#     'username': config.REDDIT_USERNAME,
#     'password': config.REDDIT_PASSWORD
# }
# headers = {
#     'User-Agent': 'MyAPI/0.0.1'
# }

# ## Save token to headers variable
# res = requests.post('https://www.reddit.com/api/v1/access_token',
#     auth = auth, data=data, headers=headers)
# TOKEN = res.json()['access_token']
# #print(TOKEN)
# headers['Authorization'] = f'bearer {TOKEN}'
# #print(headers['Authorization'])

# ## Get the top posts in Astrophotography subreddit
# res = requests.get('https://oauth.reddit.com/r/politics/hot', headers=headers)
# #print(res.json())

# ## loop through response and save relevant parts to dataframe
# for post in res.json()['data']['children']:
#     df = df.append({
#         'subreddit': post['data']['subreddit'],
#         'title': post['data']['title'],
#         'selftext': post['data']['selftext'],
#         'upvote_ratio': post['data']['upvote_ratio'],
#         'ups': post['data']['ups'],
#         'downs': post['data']['downs'],
#         'score': post['data']['score']
#     }, ignore_index=True)

#print(df)

reddit = praw.Reddit(client_id=config.REDDIT_OAUTH_CLIENT_ID,
                     client_secret=config.REDDIT_SECRET_KEY,
                     user_agent='script by u/ilikecake123',
                     redirect_uri=config.REDDIT_REDIRECT_URI,
                     refresh_token=config.REDDIT_REFRESH_TOKEN)

subr = 'ASTRONOMY_DAILY' # Choose your subreddit
title = 'THIS IS A TEST'
selftext = 'test of text post'

# subreddit = reddit.subreddit(subr) # Initialize the subreddit to a variable


# subreddit.submit(title,selftext=selftext)

image = r'C:\Users\Kevin.DESKTOP-9D0VMK8\Documents\Projects\NASA_APOD_Reddit\python_files\test.jpg'
reddit.subreddit(subr).submit_image(title, image)