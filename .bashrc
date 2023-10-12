alias gotovenv='cd /c/Users/jff20/venv'
alias python='winpty python.exe'
mcd () {
    mkdir -p $1
    cd $1
    # $1 means like user input argument i guess, and this function actually works what the heck 10_11_2023
}
venvcreate () {
    cd /c/Users/jff20/venv #enter the venv folder
    python -m virtualenv $1 # create it
    source $1/scripts/activate # activate it
    cd .. # return to the root folder
    echo "Type 'deactivate' when you're done with this Python project or switch to a different Python project."
}
top10cmd () {
    history | awk '{CMD[$2]++;count++;}END { for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | grep -v "./" | column -c3 -s " " -t | sort -nr | nl |  head -n10
    # i got this from this link https://linux.byexamples.com/archives/332/what-is-your-10-common-linux-commands/
}