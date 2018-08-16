#!/bin/bash
export XAUTHORITY=/home/nowakf/.Xauthority
export DISPLAY=':0'

notify-send "timer started" &
echo notify-send "take a break!" | at now + 25 minutes
