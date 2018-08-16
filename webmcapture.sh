#!/bin/bash
folder="$HOME/Pictures/shots/gif"

stamp=$(date +"%Y-%m-%d_%H%M%S")

beepsound="/usr/share/sounds/freedesktop/stereo/message-new-instant.oga"

beep() {
    paplay $beepsound &
}

filename=$(gdialog --title "filename?" --inputbox 200 100 2>&1)

# xrectsel from https://github.com/lolilolicon/xrectsel
geometry=$(xrectsel "--x=%x --y=%y --width=%w --height=%h") || exit -1

pipe=/tmp/gifcapture

#if pipe does not exist, make it
if [[ ! -p $pipe ]]; then
	mkfifo $pipe
fi

count=0

while true
do
	if read line <$pipe; then
		#if we get signal, either start or stop recording
		if [[ "$line" == 'signal' ]]; then
			if [[ $count > 0 ]]; then
				killall sleep
				notify-send -u normal -i info 'byzanz' 'done'
				i3 mode "default"
				beep
				break
			fi
			beep
			notify-send -u normal -i info 'Byzanz' 'started'
			#don't do more than 100s
			byzanz-record --exec='sleep 100s'  $geometry "$folder/$filename-$stamp.webm" &
			let "count++"
			continue
		elif [[ "$line" == 'abort' ]]; then
			beep
			notify-send -u normal -i info 'Byzanz' 'aborted'
			break
		fi
	fi
done

#clean up
rm -f $pipe


