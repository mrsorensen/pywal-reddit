#!/bin/bash

# -------- CONFIG ----------

# Path to subreddits file
pathToSubs=~/pywal-reddit/subreddits
# Path to the pywal-reddit.py script
pathToScript=~/pywal-reddit/pywal-reddit.py
# Maximum number of lines in rofi
maxLines=10

# ----- END OFCONFIG ------



# Subs
subs="$(cat $pathToSubs)"

# Get count of lines in subreddits file
lines="$(wc -l < $pathToSubs)"

# Don't show more lines than maxLines from config part of this script
if (( lines > maxLines )); then
	lines="$maxLines"
fi

# Get name of subreddit
input=$(echo -e "$subs" | rofi -dmenu -p "Set wallpaper from r/" -l $lines)

# Make sure user input isnt empty
if [[ "$input" == "" ]]; then
	echo "No subreddit entered"
	exit
fi

# Prompt lightmode y/n
light=$(rofi -dmenu -p "Lightmode y/n (default no)" -l 0)

# Launch pywal-reddit with lightmode if user entered y lightmode prompt
if [[ "$light" == "y" ]]; then
	python $pathToScript $input lightmode
# Else launch pywal-reddit without lightmode
else
	python $pathToScript  $input
fi

