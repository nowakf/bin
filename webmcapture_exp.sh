#!/bin/bash
folder="$HOME/Pictures/shots/gif"

stamp=$(date +"%Y-%m-%d_%H%M%S")

beepsound="/usr/share/sounds/freedesktop/stereo/message-new-instant.oga"

beep() {
paplay $beepsound &
}

filename=$(gdialog --title "filename?" --inputbox 2>&1) 

# xrectsel from https://github.com/lolilolicon/xrectsel
geometry=$(xrectsel "--x=%x --y=%y --width=%w --height=%h") || exit -1

pipe=/tmp/gifcapture
pidfile=/tmp/pidfile

#if pipe does not exist, make it
if [[ ! -p $pipe ]]; then
mkfifo $pipe
fi

count=0

#start listening for a signal
while true
do
if read line <$pipe; then
	#if we get signal, either start or stop recording
	if [[ "$line" == 'signal' ]]; then
		if [[ $count > 0 ]]; then
			pid=$(cat $pidfile)
			kill $pid
			notify-send -u normal -i info 'byzanz' 'done'
			beep
			break
		fi
		beep
		notify-send -u normal -i info 'Byzanz' 'started'
		#don't do more than 100s
		byzanz-record --exec="sh -c '((sleep 100s) & jobs -p > $pidfile)'"  $geometry "$folder/$filename-$stamp.webm" &
		let "count++"
		continue
	#allow for aborting
	elif [[ "$line" == 'abort' ]]; then
		beep
		notify-send -u normal -i info 'Byzanz' 'aborted'
		break
	fi
fi
done

i3 mode "default"
#clean up
rm -f $pipe



