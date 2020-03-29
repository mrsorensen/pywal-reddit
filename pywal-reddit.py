import requests
import json
import urllib.request
import os
import sys

# PyWals alpha opacity setting
walAlpha = 85
# Where to store images
dir = '/home/stranger/pywal-reddit/pics/'

# Check if first param is name of subreddit
if len(sys.argv) <= 2:
    print('Expects first parameter to be name of a subreddit')
    print('Expects second parameter to be hour/day/week/month/year')
    print('Example: python rwall.py earthporn day')
    sys.exit()
else:
    subreddit = sys.argv[1]

# Hour, day, week etc
if sys.argv[2] == 'hour':
    toplist = 'hour'
elif sys.argv[2] == 'day':
    toplist = 'day'
elif sys.argv[2] == 'week':
    toplist = 'week'
elif sys.argv[2] == 'month':
    toplist = 'month'
else:
    toplist = 'year'

# URL to subreddits json
URL = 'http://reddit.com/r/{}/top.json?t={}'.format(subreddit, toplist)

# Store http request as json
data = requests.get(URL, headers = {'User-agent':'rwall'}).json()

# Check if valid subreddit
if not data['data']['children']:
    print('Subreddit not found')
    sys.exit()

# Get first image from subreddit
imgurl = data['data']['children'][0]['data']['url']

# Checks if image url is image
if imgurl.lower().endswith(('.jpg', '.png')):
    # Full path to stored file
    fullfilename = os.path.join(dir, os.path.basename(imgurl))
    # Stores image 
    urllib.request.urlretrieve(imgurl, fullfilename)
    # Set as wallpaper
    os.system('wal -a {} -i {} > /dev/null'.format(walAlpha, fullfilename))
else:
    print('Couldn\'t get image')
