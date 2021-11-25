import config
import praw

def reddit_uploader(info):
    reddit = praw.Reddit(client_id=config.REDDIT_OAUTH_CLIENT_ID,
                        client_secret=config.REDDIT_SECRET_KEY,
                        user_agent='script by u/ilikecake123',
                        redirect_uri=config.REDDIT_REDIRECT_URI,
                        refresh_token=config.REDDIT_REFRESH_TOKEN)

    subr = 'ASTRONOMY_DAILY' # Choose your subreddit

    image = r'C:\temp\test.jpg'
    reddit.subreddit(subr).submit_image(info[0], image)

if __name__ == "__main__":
   reddit_uploader()