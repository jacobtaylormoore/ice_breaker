from dotenv import load_dotenv
import os

load_dotenv()

from twitter.extract_text_only import extract_tweet_data

# Scrape twitter using apify tool 
def scrape_user_tweets(username, num_tweets=5, mock: bool = False):
    """scrape twitter using apify

    Args:
        username (_type_): twitter username
        num_tweets (int, optional): number of tweets to scrape. Defaults to 5.
        mock (bool, optional): real scrape or test so as not to use up tokens. Defaults to False.
    """

# Pull text, createdAt, and url
def text_only(limit=0):
    extract_tweet_data(limit=limit, include_date=False)




if __name__ == '__main__':
    text_only(limit=200)
    print(text_only)


