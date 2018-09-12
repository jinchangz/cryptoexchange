#!/bin/bash

processName="shell.py"
restartCmd="python shell.py &"
interval=10

array=(price_margin.py get_cc_ticker.py get_bf_ticker.py get_bb_ticker.py get_qx_ticker.py get_zf_ticker.py)
#echo ${array[1]}
while true
do
    for v in "${array[@]}"
    do
        isAlive=`ps -ef | grep "$v" | grep -v grep | wc -l`
        if [ $isAlive = 1 ]; then
            echo "Server is running."
        else
            echo "Server is dead, restarting..."
            python $v &
        fi
    done
    sleep $interval
done