import os
import time
import tweepy
import json
from shutil import move


class log:
    def info(text: str):
        print(f"[Info] {text}")
    def success(text: str):
        print(f"[Success] {text}")
    def error(text: str):
        print(f"[Error] {text}")
# The class for outputting console logs.

try:
    with open("config.json", "r") as unloaded_config:
        config = json.load(unloaded_config)
        log.success("Config has been loaded")
except:
    log.error("Config could not be loaded")
    exit()
# Loads the config.

# Twitter API credentials
consumer_key = config["consumerKey"]
consumer_secret = config["consumerSecret"]
access_token = config["accessTokenKey"]
access_token_secret = config["accessTokenSecret"]


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
image_dir = config["directory"]
published_dir = config["directory_pub"]

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
            tweet = config["tweetContent"]
            # Post tweet with image
            client.create_tweet(text=tweet, media_ids=[media.media_id], reply_settings='mentionedUsers')
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
    time.sleep(config["sleepTime"])
