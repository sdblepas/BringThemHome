# BringThemHome
# BringThemHomeNow Twitter Bot

## Overview
This script is designed to automate the process of tweeting images with a specific hashtag, counting the days since a particular date, and providing a precise duration in years, months, weeks, and days. It's particularly tailored for campaigns or movements that aim to raise awareness over time through social media, specifically Twitter.

## Features
- **Automated Tweeting**: Automatically tweets images from a specified directory with a custom message that includes the total number of days and a formatted duration since a specific start date.
- **Image Management**: After tweeting an image, it moves the image to a "published" directory to avoid re-posting. If the source directory is empty, it moves all images back from the "published" directory to be tweeted again.
- **Precise Duration Calculation**: Calculates the exact duration since a specified date in years, months, weeks, and days.
- **Twitter API Integration**: Uses the Tweepy library for Twitter API integration, allowing for media uploads and tweet posting.

## Requirements
- Python 3.x
- Tweepy library (`pip install tweepy`)

## Setup
1. **Twitter Developer Account**: You need a Twitter Developer account and a project/app created within it to get your API keys and tokens.
2. **Install Dependencies**: Run `pip install tweepy` to install the necessary Python library.
3. **Configure API Keys**: Replace the placeholder values for `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret` in the script with your actual Twitter API credentials.

## Usage
1. **Set the Start Date**: Modify the `precise_duration_since("07 October 2023")` call in the `tweet_image` function to your campaign's start date.
2. **Specify Image Directories**: Update the `image_dir` and `published_dir` variables with the paths to your source and published image directories, respectively.
3. **Run the Script**: Execute the script with Python. It will continuously run, tweeting an image every hour. Adjust the `time.sleep(3600)` call at the end of the script if you wish to change the frequency.

## Important Notes
- **Security**: Do not share your API keys and tokens publicly. Keep them secure and private.
- **Rate Limits**: Be aware of Twitter's rate limits for API usage to avoid getting your account suspended.
- **Image Formats**: The script currently supports `.png`, `.jpg`, and `.jpeg` image formats. Ensure your images are in these formats.

## License
This project is open-source and available under the MIT License. Feel free to fork, modify, and use it in your campaigns or projects.

## Disclaimer
This script is provided as is, without warranty of any kind. Use it at your own risk. The author is not responsible for any consequences arising from its use.


## Configuration

You need to add the proper credentials and folder path in the config.json

    {
        "consumerKey" : "",
        "consumerSecret" : "",
        "accessTokenKey" : "",
        "accessTokenSecret" : "",
        "directory" : "<PATH>>",
        "directory_pub" : "PATH",
        "sleepTime" : 3600,
        "tweetContent" : "#BringThemBackNow"
    }
