#!/bin/bash

processName="shell.py"
restartCmd="python shell.py &"
interval=10

array=(`cat participant.txt|xargs`) 
echo ${array[1]}
while true
do
    for v in "${array[@]}"
    do
        isAlive=`ps -ef | grep "$v" | grep -v grep | wc -l`
        if [ $isAlive = 1 ]; then
            echo "Server is running."
        else
            echo "Server is dead, restarting..."
            python3 $v &
        fi
    done
    sleep $interval
done