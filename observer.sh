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
<<<<<<< HEAD
            :
=======
<<<<<<< HEAD
            :
=======
            # echo "Server is running."
>>>>>>> 6dfd687bdd378b2a711264808d41de2616351f0f
>>>>>>> d7abe9a674032b1e285d1daa16bc2d4671b0a94e
        else
            echo "Server is dead, restarting..."
            python3 $v &
        fi
    done
    sleep $interval
done