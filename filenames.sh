#!/bin/bash 

sed 's/ /_/g' | sed $'s/\'//g' | sed $'s/\`//g' | sed 's/_-_/_/g' | sed 's/_\+/_/g'
