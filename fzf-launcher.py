#!/usr/bin/python

import subprocess, os, shlex, sys, asyncio

class LsBin:
    def prefix():
        pathdirs = os.environ['PATH'].split(':')
        return sep(get_files(pathdirs, test = lambda x: os.access(x, os.X_OK)))
    def suffix(argument):
        return argument

class LsDoc:
    docpath = '/home/francis/Documents/z-n.0.01/'
    def prefix():
        return sep(get_files([LsDoc.docpath]))
    def suffix(argument):
        return 'gvim '+LsDoc.docpath+argument

def get_files(dirs, test = None):
    files = dict()
    out = ""
    for d in dirs:
        dirfiles = os.listdir(d)
        for f in dirfiles:
            if test != None:
                if test(d+'/'+f):
                    files[f] = d
            else:
                files[f] = d
    return sort_files(files)

def sep(flist):
    out = ""
    for u in flist:
        out += u.rsplit('/', 1)[1] + '\n'
    return 'echo '+ shlex.quote(out)

def sort_files(files):
    listoffiles = []
    for f, path in files.items():
        listoffiles.append(path+'/'+f)
    return sorted(listoffiles, key=os.path.getatime)


commands = [ LsBin, LsDoc ]
def rec_call_fzf(index):
    command = commands[index].prefix()+ ' | fzf \
            --tiebreak="index" --tac\
           --bind "tab:abort+execute(echo -n next)" \
           --bind "btab:abort+execute(echo -n prev)" \
           --bind "esc:abort+execute(echo -n quit)"'
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    out = process.stdout.decode('utf-8')
    if out == "next":
        rec_call_fzf((index + 1) % len(commands))
    elif out == "prev":
        rec_call_fzf((index - 1) % len(commands))
    elif out == "quit":
        exit(0)
    else:
        proc = subprocess.Popen(shlex.split(commands[index].suffix(out)), start_new_session=True)
        return

def main():
    rec_call_fzf(0)

main()
