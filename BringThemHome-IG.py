import os
import time
from shutil import move
from instagrapi import Client

# Instagram API credentials
username = ""
password = "#"


class log:
    def info(text: str):
        print(f"[Info] {text}")
    def success(text: str):
        print(f"[Success] {text}")
    def error(text: str):
        print(f"[Error] {text}")
# The class for outputting console logs.


# Create API object
api = Client()
api.login(username, password)

log.info(f"User: {api.user_id}")

# Directory containing images to be posted
image_dir = "/Users/benjamin/PycharmProjects/BringThemHome/Images"
published_dir = "/Users/benjamin/PycharmProjects/BringThemHome/Images_pub"

def post_image():
    for image in os.listdir(image_dir):
        if image.endswith(('.png', '.jpg', '.jpeg')):
            # Upload image
            text = "#BringThemHome"
            media = api.photo_upload(f"{image_dir}/{image}", caption=text)
            log.info(f"Media: {media}")
            filename = image_dir + image
            log.info(f"Filename: {filename}")
            # Post image with caption
            # api.photo_upload(media, caption=text)
            move(f"{image_dir}/{image}", f"{published_dir}/{image}")
            break

while True:
    if not os.listdir(image_dir):  # if image directory is empty
        # move all images back from published to image directory
        for image in os.listdir(published_dir):
            if image.endswith(('.png', '.jpg', '.jpeg')):
                move(f"{published_dir}/{image}", f"{image_dir}/{image}")
    post_image()
    time.sleep(60)  # Sleep for 60 seconds before posting the next image