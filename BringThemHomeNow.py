import os
import time
import tweepy
from shutil import move


class log:
    def info(text: str):
        print(f"[Info] {text}")
    def success(text: str):
        print(f"[Success] {text}")
    def error(text: str):
        print(f"[Error] {text}")
# The class for outputting console logs.


# Twitter API credentials
consumer_key = 'dXpYSxZsdZsAHW5dJOoVp4K1y'
consumer_secret = 'eEm2CBbHerEh0H1hGxOdbtKNRt9pZItE81ZmwdzKWv3MVNuSSQ'
access_token = '17509196-w7xWuphmwMiVVticFWODAJGMX6t0PHwHCqQzRMtLZ'
access_token_secret = 'OInqaJpWUaqhUfP0ZDcXhohyNDR8dVge1bIchB3tkT3vj'
#access_token = 'c3ZSTU9WMjZtRFFmYW85MmU5ZmE6MTpjaQ'
#access_token_secret = 'ydSd7v8u-A2L8f0fXsK5jGNZDAEBFFxze0SJGwFKKti7c9e4r3'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret )
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)
log.success("Connected to the Twitter API")
log.info(f"User: {api.verify_credentials().screen_name}")
log.info(f"Followers: {api.verify_credentials().followers_count}")
time.sleep(1)

# Directory containing images to be tweeted
image_dir = '/Users/benjamin/BringThemHomeNow/Otages/'
published_dir = '/Users/benjamin/BringThemHomeNow/Otages_pub/'

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)


log.info(f"Client: {client.consumer_key}")


def tweet_image():
    for image in os.listdir(image_dir):
        if image.endswith(('.png', '.jpg', '.jpeg')):
            # Upload image
            media = api.media_upload(f"{image_dir}/{image}")
            media_ids = [media.media_id]
            log.info(f"Media: {media}")
            filename = image_dir + image
            log.info(f"Filename: {filename}")
            tweet = "#BringThemHomeNow"
            # Post tweet with image
            client.create_tweet(text=tweet, media_ids=[media.media_id])
            #api.update_status(status=tweet, media_ids=media_ids)
            move(f"{image_dir}/{image}", f"{published_dir}/{image}")
            break


while True:
    if not os.listdir(image_dir):  # if image directory is empty
        # move all images back from published to image directory
        for image in os.listdir(published_dir):
            if image.endswith(('.png', '.jpg', '.jpeg')):
                move(f"{published_dir}/{image}", f"{image_dir}/{image}")
    tweet_image()
    time.sleep(3600)
