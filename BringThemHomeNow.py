import os
import time
import tweepy
from shutil import move
from datetime import datetime

class log:
    def info(text: str):
        print(f"[Info] {text}")
    def success(text: str):
        print(f"[Success] {text}")
    def error(text: str):
        print(f"[Error] {text}")
# The class for outputting console logs.

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
image_dir = '/volume1/home/admin/BringThemHome/Otages/'
published_dir = '/volume1/home/admin/BringThemHome/Otages_pub/'

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

log.info(f"Client: {client.consumer_key}")

from datetime import datetime

def precise_duration_since(start_date_str):
    start_date = datetime.strptime(start_date_str, "%d %B %Y")
    current_date = datetime.now()
    total_days = (current_date - start_date).days

    # Initialize counters
    years = 0
    months = 0
    days = total_days  # Use total_days to keep track of remaining days

    # Calculate years
    while True:
        next_year_date = start_date.replace(year=start_date.year + 1)
        if next_year_date <= current_date:
            years += 1
            days -= (next_year_date - start_date).days
            start_date = next_year_date
        else:
            break

    # Calculate months
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0):
        month_lengths[1] = 29  # February in a leap year

    while days >= month_lengths[start_date.month - 1]:
        days -= month_lengths[start_date.month - 1]
        months += 1
        if start_date.month == 12:
            start_date = start_date.replace(month=1, year=start_date.year + 1)
            if start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0):
                month_lengths[1] = 29  # Adjust for leap year
            else:
                month_lengths[1] = 28
        else:
            start_date = start_date.replace(month=start_date.month + 1)

    # Calculate weeks and days
    weeks = days // 7
    days_left = days % 7

    # Build the formatted_duration string conditionally with singular and plural forms
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    if weeks > 0:
        parts.append(f"{weeks} week{'s' if weeks > 1 else ''}")
    if days_left > 0:
        parts.append(f"{days_left} day{'s' if days_left > 1 else ''}")

    formatted_duration = ", ".join(parts)

    return total_days, formatted_duration

def tweet_image():
    total_days, formatted_duration = precise_duration_since("07 October 2023")  # Calculate precise duration
    total_days += 6  # Add 6 to total_days
    for image in os.listdir(image_dir):
        if image.endswith(('.png', '.jpg', '.jpeg')):
            # Upload image
            media = api.media_upload(f"{image_dir}/{image}")
            media_ids = [media.media_id]
            log.info(f"Media: {media}")
            filename = image_dir + image
            log.info(f"Filename: {filename}")
            # Include both the total number of days and the formatted duration in the tweet
            tweet = f"#BringThemHomeNow #{total_days}October. Since #7October ({formatted_duration})"
            #print(f"Tweet would be: {tweet} with media ID: {media_ids[0]}")
            # Uncomment the next line to post the tweet when ready
            client.create_tweet(text=tweet, media_ids=[media.media_id], reply_settings='mentionedUsers')
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
