#!/usr/bin/python

import shlex, subprocess

prefixes = [
        ('fzf-menu', 'exec'),
        ('ls', 'echo')
        ]

def recurse(index):

    command = prefixes[index][0]+ ' | ' + 'fzf     \
           --bind "tab:abort+execute(echo next)" \
           --bind "btab:abort+execute(echo prev)" \
           --bind "esc:abort+execute(echo quit)"'
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    out = process.stdout.decode('utf-8')
    print(out)
    if out == "next":
        recurse((index + 1) % len(prefixes))
    elif out == "prev":
        recurse((index - 1) % len(prefixes))
    elif out == "quit":
        exit(0)
    else:
        subprocess.run(prefixes[index][1]+' '+out, shell=True)

recurse(0)
