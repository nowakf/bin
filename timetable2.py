#!/usr/bin/python

import datetime
import os
import tasklib

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

now = datetime.datetime.now()

def notaday():
    print("very strange - this isn't a day")

def notaworkhour():
    print("only work hous are defined- change the crontab")

def monday(time):
    hours = {
            9: "creative",
            10: "",
            11: "",
            12: "",
            13: "german",
            14: "Eat lunch",
            15: "physical",
            16: "",
            17: "writing",
            18: "start cooking supper"
            }
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def tuesday(time):
    hours = {
            9: "creative",
            10: "",
            11: "",
            12: "",
            13: "german",
            14: "Eat lunch",
            15: "physical",
            16: "",
            17: "shopping",
            18: "start cooking supper"
            }
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def wednesday(time):
    hours = {
            9: "creative",
            10: "",
            11: "",
            12: "",
            13: "german",
            14: "Eat lunch",
            15: "physical",
            16: "",
            17: "writing",
            18: "start cooking supper"
            }
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def thursday(time):
    hours = {
            9: "creative",
            10: "",
            11: "",
            12: "",
            13: "german",
            14: "Eat lunch",
            15: "physical",
            16: "",
            17: "writing",
            18: ""
            }
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def friday(time):
    hours = {
            9: "creative",
            10: "",
            11: "",
            12: "",
            13: "german",
            14: "Eat lunch",
            15: "physical",
            16: "",
            17: "writing",
            18: ""
            }
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def saturday(time):
    hours = {
            9: "",
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
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def sunday(time):
    hours = {
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
    try:
        alert(hours[time], time)
    except KeyError:
        notaworkhour()

def playsound(filename):
    path = "~/Music/hoursounds/"
    extension = ".ogg"
    if os.path.isfile('paplay '+path+filename+extension):
        os.system(path+filename+extension)
    else:
        os.system('paplay '+path+"default"+extension)

projects = {
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
    days[now.today().weekday()](now.hour)

except KeyError:
    print(now.today().weekday())
    notaday()
