"""Module designed to automate tweeting images for awareness campaigns."""

import os
import time
from datetime import datetime
from shutil import move
import tweepy

class Log:
    """Class for outputting console logs."""
    
    @staticmethod
    def info(text: str):
        """Logs informational messages."""
        print(f"[Info] {text}")
    
    @staticmethod
    def success(text: str):
        """Logs success messages."""
        print(f"[Success] {text}")
    
    @staticmethod
    def error(text: str):
        """Logs error messages."""
        print(f"[Error] {text}")

# Twitter API credentials
consumer_key = config["consumerKey"]
consumer_secret = config["consumerSecret"]
access_token = config["accessTokenKey"]
access_token_secret = config["accessTokenSecret"]

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
log = Log()
log.success("Connected to the Twitter API")
log.info(f"User: {api.verify_credentials().screen_name}")
log.info(f"Followers: {api.verify_credentials().followers_count}")
time.sleep(1)

# Directory containing images to be tweeted
IMAGE_DIR = '/volume1/home/admin/BringThemHome/Otages/'
PUBLISHED_DIR = '/volume1/home/admin/BringThemHome/Otages_pub/'

def precise_duration_since(start_date_str: str) -> tuple:
    """Calculates the precise duration since a given start date."""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    current_date = datetime.now()
    total_days = (current_date - start_date).days

    years, months, days = 0, 0, total_days
    while True:
        try:
            next_year_date = start_date.replace(year=start_date.year + 1)
        except ValueError:
            break
        if next_year_date <= current_date:
            years += 1
            days -= (next_year_date - start_date).days
            start_date = next_year_date
        else:
            break

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if start_date.year % 4 == 0 and (start_date.year % 100 != 0 or start_date.year % 400 == 0):
        month_lengths[1] = 29

    for month_length in month_lengths[start_date.month - 1:]:
        if days >= month_length:
            days -= month_length
            months += 1
        else:
            break

    weeks = days // 7
    days = days % 7

    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    if weeks > 0:
        parts.append(f"{weeks} week{'s' if weeks > 1 else ''}")
    if days > 0:
        parts.append(f"{days} day{'s' if days > 1 else ''}")

    formatted_duration = ', '.join(parts)
    return total_days, formatted_duration

def tweet_image():
    """Tweets an image with a message including the duration since a specific start date."""
    images = [img for img in os.listdir(IMAGE_DIR) if img.endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        log.info("No images to tweet. Moving published images"
                  "back to the source directory.")
        for img in os.listdir(PUBLISHED_DIR):
            move(os.path.join(PUBLISHED_DIR, img), os.path.join(IMAGE_DIR, img))
        images = os.listdir(IMAGE_DIR)

    if images:
        image_path = os.path.join(IMAGE_DIR, images[0])
        total_days, formatted_duration = precise_duration_since("2023-10-07")
        status = f"Bringing them home, day {total_days}. Duration: {formatted_duration}. #BringThemHomeNow"
        api.update_status_with_media(status=status, filename=image_path)
        move(image_path, os.path.join(PUBLISHED_DIR, images[0]))
        log.success(f"Tweeted: {status}")
    else:
        log.error("No images available to tweet.")

if __name__ == "__main__":
    while True:
        tweet_image()
        log.info("Waiting for the next tweet.")
        time.sleep(3600)  # Wait for 1 hour before tweeting again
