import config
import requests
import pandas

## Create variable for pandas dataframes
df = pandas.DataFrame()

## Create variables for reddit connection
auth = requests.auth.HTTPBasicAuth(config.REDDIT_OAUTH_CLIENT_ID, config.REDDIT_SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': config.REDDIT_USERNAME,
    'password': config.REDDIT_PASSWORD
}
headers = {
    'User-Agent': 'MyAPI/0.0.1'
}

## Save token to headers variable
res = requests.post('https://www.reddit.com/api/v1/access_token',
    auth = auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
print(TOKEN)
headers['Authorization'] = f'bearer {TOKEN}'
print(headers['Authorization'])

## Get the top posts in Astrophotography subreddit
res = requests.get('https://oauth.reddit.com/r/astrophotograhy/hot',headers=headers)
# print(res.json())
for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)

print(df)