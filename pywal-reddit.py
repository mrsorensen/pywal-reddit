#!/usr/bin/python

# ------- USER CONFIG -----------

# PyWals opacity option (set to 0 for full transparency or 100 for no transparency)
alpha = 85
# Where to storage downloaded images
directory = '~/Pictures/Reddit-Wall/'
# Set this to True/False to run neofetch --w3m with new wallpaper when done
neofetch = True

# ------- END CONFIG ------------




# Imports
from os.path import expanduser
import requests
import os
import sys
import urllib.request
import re

# Change ~/Folder to /home/yourusername/Folder
directory = expanduser(directory)

# Get name of current wallpaper
curWall = os.popen('sed 1d "$HOME/.fehbg"').read()
curWall = os.path.basename(re.search('''(?<=')\s*[^']+?\s*(?=')''', curWall).group())

# Create folder for pictures if not already created
if not os.path.exists(directory):
    os.makedirs(directory)

# Exit if no subreddit as parameter
if len(sys.argv) < 2:
    print('First paramter should be name of a subreddit')
    print('Ex: ./reddit-wall earthporn')
    print('Enable lightmode with ./reddit-wall earthporn lightmode')
    sys.exit()

# Set lightmode if second parameter is set
if len(sys.argv) >= 3:
    lightmode = '-l'
else:
    lightmode = ''

# Set subreddit to first parameter
subreddit = sys.argv[1]

# URL to subreddits json
URL = 'http://reddit.com/r/{}.json'.format(subreddit)

# Store JSON
data = requests.get(URL, headers = {'User-agent':'reddit-wall'}).json()

# Validate subreddit
if not data['data']['children']:
    print('r/{} not found'.format(subreddit))

# Find first post with image attached in JSON response
for post in data['data']['children']:
    if post['data']['url'].lower().endswith(('.jpeg', '.jpg', '.png')):
        if os.path.isfile(os.path.join(directory, os.path.basename(post['data']['url']))):
            print('Skipping {}'.format(os.path.basename(post['data']['url'])))
        else:
            imgURL = post['data']['url']
            print('Preparing image {} ...'.format(imgURL))
            break

# Check if image was found in subreddit
try:
    imgURL
except NameError:
    print('No image found in r/{}'.format(subreddit))
    sys.exit()

# Path to locally store image
pathToImg = os.path.join(directory, os.path.basename(imgURL))

# Store image
if urllib.request.urlretrieve(imgURL, pathToImg):
    print('Image stored in {}'.format(pathToImg))
else:
    print('There was an unexpected problem')

# Set wallpaper
os.system('wal {} -a {} -i {} > /dev/null'.format(lightmode, alpha, pathToImg))
# Confirm new wallpaper
if neofetch:
    os.system('neofetch --size 30% --w3m {}'.format(pathToImg))
else:
    print('New wallpaper is {}'.format(os.path.basename(pathToImg)))
