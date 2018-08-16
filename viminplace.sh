#!/bin/sh
_INPUT_FILE=$(mktemp).txt
POSTS_PATH="/home/francis/Documents/posts.txt"
# i3 will make this a scratch window based on the class.
i3 split v
i3-sensible-terminal -e vim -c "startinsert | set noswapfile | set wrap linebreak nolist | Goyo" "$_INPUT_FILE"
sleep 0.1
# strip last byte, the newline. https://stackoverflow.com/a/12579554
head -c -1 $_INPUT_FILE | xsel -i -b |xdotool key ctrl+v
echo "---------" $(date +%Y/%m/%d) >> $POSTS_PATH
cat $_INPUT_FILE >> $POSTS_PATH
rm $_INPUT_FILE
