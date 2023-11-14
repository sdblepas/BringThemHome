import os
import time
from shutil import move
import requests

# Facebook API credentials
access_token = "your_access_token"

# Directory containing images to be posted
image_dir = "path_to_image_directory"
published_dir = "path_to_published_directory"

def post_image():
    for image in os.listdir(image_dir):
        if image.endswith(('.png', '.jpg', '.jpeg')):
            # Upload image
            files = {'file': open(f"{image_dir}/{image}", 'rb')}
            response = requests.post(
                f"https://graph.facebook.com/v12.0/me/photos?access_token={access_token}",
                files=files
            )
            media_id = response.json().get('id')
            log.info(f"Media ID: {media_id}")
            caption = "Your caption here"
            # Post image with caption
            params = {
                'access_token': access_token,
                'caption': caption,
                'attached_media': f'{{"media_fbid":"{media_id}"}}'
            }
            response = requests.post(
                "https://graph.facebook.com/v12.0/me/feed",
                params=params
            )
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