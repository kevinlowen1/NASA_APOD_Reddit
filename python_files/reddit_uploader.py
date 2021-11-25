import config
import praw

###praw documenation
#https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html?highlight=submit#praw.models.Subreddit.submit_image

def reddit_uploader(info):
    reddit = praw.Reddit(client_id=config.REDDIT_OAUTH_CLIENT_ID,
                        client_secret=config.REDDIT_SECRET_KEY,
                        user_agent='script by u/ilikecake123',
                        redirect_uri=config.REDDIT_REDIRECT_URI,
                        refresh_token=config.REDDIT_REFRESH_TOKEN)

    subr = 'ASTRONOMY_DAILY' # Choose your subreddit

    if(info[5] == 'video'):
        print('video APOD, wtf dude')
        reddit.subreddit(subr).submit(info[0], info[1])
    else:
        print('continuing as normal, photo APOD')
        image = r'C:\temp\test.jpg'
        reddit.subreddit(subr).submit_image(info[0], image)

if __name__ == "__main__":
   reddit_uploader()