import psutil
import tweepy


didicode = "Code.exe" in (i.name() for i in psutil.process_iter())

CONSUMER_KEY = "ajFV7QOPFseG3wq7GteJ6B3ke"
CONSUMER_SECRET = "nwGh5ANoEKTa9baa77zZhcf6UC8O3G3vQn62x4wYjjNzRKRsD5"
ACCESS_TOKEN = "1506129662186954757-Keg4O2dUctPDj8t7Zq8xaODVXIG1ue"
ACCESS_SECRET = "ktInGwm8arFOUEZ7ZsazJzhkkvf4mrQEdtbv6YTlP0mjD"
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAIz8aQEAAAAAMFfMMG%2F2gXhVufaHWMO9hxGQGUY%3D8PuXSx14REctDs5vTzxKoRSzhoL6KrZI5DVndLyp5OH1zsKtLH"

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


