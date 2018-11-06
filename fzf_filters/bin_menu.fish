#!/bin/fish
if [ $argv = 'prefix' ]
    for p in $PATH
        ls $p
    end
else if [ $argv = 'suffix' ]
    echo -n exec
end
