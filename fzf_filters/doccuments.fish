#!/bin/fish
if [ $argv = 'prefix' ]
    for p in /home/francis/Documents
        ls $p
    end
else if [ $argv = 'suffix' ]
    echo -n vim
end
