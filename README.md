# BringThemHome
Here's an overview of what the script does:

1. It imports the required libraries, including os, tweepy, and shutil.
2. It sets up the Twitter API credentials, including the consumer key, consumer secret, client ID, and client secret.
3. It authenticates to the Twitter API using the provided credentials.
4. The script defines two directories: image_dir and published_dir. These directories represent the source directory where images to be tweeted are stored (image_dir) and the destination directory where successfully tweeted images are moved to (published_dir).
5. The script defines a function named tweet_image() that performs the following steps:
- It retrieves a list of images from the image_dir directory.
- It iterates over the images and selects the first image that has a valid file extension (.png, .jpg, or .jpeg).
- It uploads the selected image to Twitter using the Tweepy media_upload() method and retrieves the media ID of the uploaded image.
- It posts a tweet with the uploaded image using the Tweepy update_status() method, including the media ID.
- If the tweet is successfully posted, it moves the tweeted image from the image_dir directory to the published_dir directory.
6. The script contains a loop that continuously calls the tweet_image() function. It checks if the image_dir directory is empty, and if so, it moves all images from the published_dir directory back to the image_dir directory. This ensures a continuous cycle of tweeting images from the image_dir directory.

Overall, the script automates the process of tweeting images with the hashtag "#BringThemHomeNow" by continuously checking for new images in the image_dir directory, uploading them to Twitter, and moving successfully tweeted images to the published_dir directory.

