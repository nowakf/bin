#!/usr/bin/python

import os
import sys

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

text = "Take a five-minute break."

os.system('notify-send "'+text+'"')
