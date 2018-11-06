#! /bin/bash
commands=(fzf_bin fzf_exec  \
          fzf_docs fzf_gvim \
          fzf_mpc fzf_play )

freq_file=~/.local/share/fzf_launcher/freq_file.txt

main() {
  if selection=$( ${commands[$1]} | fzf_args ); then
    #if we have a result, then run it,  
    ${commands[$[$1 + 1]]} $selection 
  else
     #else, iterate through the array of commands
    if   [[ $selection == "next" ]]; then
          main $[($1 + 2) % ${#commands[@]}]
    elif [[ $selection == "prev" ]]; then
          main $[($1 - 2) % ${#commands[@]}]
    else
          echo $selection + foo
          exit
    fi
  fi
}

fzf_bin() {
  tac $freq_file | grep 'bin#' | strip_prefix 
  ls -c /usr/share/applications | sed 's/\(.*\)\..*/\0:\1/'
}

fzf_exec() {
  echo bin#$1 >> $freq_file
  setsid gtk-launch $(echo $1 | strip_suffix) 2> /dev/null && clean_up
}

strip_prefix() {
  sed 's/[^ #]*#//g'
}

strip_suffix() {
  sed 's/:[^ :]*//g'
}

fzf_docs() {
  tac $freq_file | grep 'doc' | strip_prefix 
  find ~/Documents -type f | sed 's/\/\([^/]*$\)/\0:\1/' | grep -v '\.pdf\|\.mobi\|\.epub'
}
fzf_gvim() {
  echo doc#$1 >> $freq_file
  gvim $(echo $@ | strip_prefix | strip_suffix ) 2>/dev/null
}

fzf_mpc() {
  mpc listall | sed 's/.*/\0:\0/'
}

fzf_play(){
  mpc clear
  for i in $(echo $@ | strip_suffix); do
	  mpc add $i
  done
  mpc play
}

fzf_args() {
  awk '!a[$0]++' | fzf --tiebreak="index"      \
    --delimiter=: --with-nth=2 -m --no-clear   \
    --bind "right:abort+execute(echo -n next)" \
    --bind "left:abort+execute(echo -n prev)"  \
    --bind "esc:abort+execute(echo -n quit)"
}

clean_up() {
  #don't know why, but window sometimes hangs around
  awk '!a[$0]++' $freq_file > $freq_file.tmp && cp $freq_file.tmp $freq_file
  wmctrl -lp | awk '/fzf-menu/{print $3}' | xargs kill
}

main 0

