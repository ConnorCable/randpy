import psutil
import tweepy


didicode = "Code.exe" in (i.name() for i in psutil.process_iter())

CONSUMER_KEY = "########"
CONSUMER_SECRET = "########"
ACCESS_TOKEN = "########"
ACCESS_SECRET = "########"
BEARER_TOKEN = r"########"

client = tweepy.Client(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_SECRET)

def poster():
    if didicode:
        response = client.create_tweet(
        text = "I coded today!"
    )
    else: 
        response = client.create_tweet(
        text = "I didn't code today! I'm probably playing Valheim instead! I'm a slacker!"
    )
    print("I tweeted!")


