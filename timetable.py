#!/usr/bin/python

import datetime
import os
import tasklib

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

now = datetime.datetime.now()


def day(day, time):
    try:
        alert(day[time], time)
    except KeyError:
        print("only work hous are defined- change the crontab")

monday = {
        9: "creative",
        10: "creative",
        11: "creative",
        12: "research",
        13: "german",
        14: "Eat lunch",
        15: "physical",
        16: "maths",
        17: "writing",
        18: "start cooking supper"
        }

tuesday = {
        9: "creative",
        10: "creative",
        11: "creative",
        12: "research",
        13: "german",
        14: "Eat lunch",
        15: "physical",
        16: "maths",
        17: "shopping",
        18: "start cooking supper"
        }

wednesday = {
        9: "creative",
        10: "creative",
        11: "creative",
        12: "research",
        13: "german",
        14: "Eat lunch",
        15: "physical",
        16: "maths",
        17: "writing",
        18: "start cooking supper"
        }

thursday = {
        9: "creative",
        10: "creative",
        11: "creative",
        12: "research",
        13: "german",
        14: "Eat lunch",
        15: "physical",
        16: "electronics",
        17: "writing",
        18: "writing"
        }

friday = {
        9: "creative",
        10: "creative",
        11: "creative",
        12: "research",
        13: "german",
        14: "Eat lunch",
        15: "physical",
        16: "electronics",
        17: "writing",
        18: "writing"
        }

saturday = {
        9: "algorithms",
        10: "",
        11: "",
        12: "Do household stuff",
        13: "",
        14: "Eat lunch",
        15: "",
        16: "shopping",
        17: "writing",
        18: ""
        }

sunday = {
        9: "",
        10: "",
        11: "",
        12: "",
        13: "",
        14: "Eat lunch",
        15: "",
        16: "",
        17: "writing",
        18: "start cooking supper",
        }

def playsound(filename):
    path = "~/Music/hoursounds/"
    extension = ".ogg"
    if os.path.isfile('paplay '+path+filename+extension):
        os.system(path+filename+extension)
    else:
        os.system('paplay '+path+"default"+extension)

projects = {
        "research"
        "algorithm"
        "writing",
        "german",
        "creative",
        "household",
        "shopping",
        "physical"
        }

def alert(scheduleEntry, time):
    if scheduleEntry == "":
        os.system('notify-send '+"'take a long break!'")
    elif scheduleEntry in projects:
        os.system('notify-send "'+scheduleEntry+'"')

        tw = tasklib.TaskWarrior(data_location='~/.task', create=False)
        
        tasks = tw.tasks.filter(status='pending', project=scheduleEntry)

  
        if len(tasks) > 0:
            for task in tasks:
                os.system('notify-send '+str(task))
        else:
            os.system('notify-send '+"'no "+scheduleEntry+" tasks left'")
    else:
        os.system('notify-send "'+scheduleEntry+'"')

    playsound(scheduleEntry)


days = {
        0: monday,
        1: tuesday,
        2: wednesday,
        3: thursday,
        4: friday,
        5: saturday,
        6: sunday
        }

try:
    day(days[now.today().weekday()], now.hour)

except KeyError:
    print("very strange - this isn't a day")
