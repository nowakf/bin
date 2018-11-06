#! /usr/bin/env fish

function bin_fzf
    for p in $PATH
        ls $p
    end
end

set commands bin_fzf exec \
             bin_fzf echo

function call_fzf
    set index 0
    while true
        set out $commands[$index] | fzf \
           --bind "tab:abort+execute(echo next)" \
           --bind "btab:abort+execute(echo prev)" \
           --bind "esc:abort+execute(echo quit)"

        switch ($out)
        case next
            set index (math '($index + 1) % count $commands')
        case prev
            set index (math '($index - 1) % count $commands')
        case quit
            break
        case '*'
            echo malformed
        end
    end
end

call_fzf

