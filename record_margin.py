import pandas as pd
import json
from pprint import pprint
import sys
import subprocess
from datetime import datetime
import itertools
import linecache
import os
import time

interval = 1

def get_margin(ex1, ex2):
    margin = 0
    if not(isinstance(ex1['last'], float) or isinstance(ex2['last'], float)):
        sys.exit()

    if ex1['last'] != 0 and ex2['last'] != 0:
        if ex1['last'] >= ex2['last']:
            margin = ex1['ask'] - ex2['bid']
        else:
            margin = ex1['ask'] - ex2['bid']
    else:
        sys.exit()


    return margin

def get_exchange(ex):
    with open('tickers/'+ ex + '_ticker.json') as f:
        exchange = json.load(f)
        exchange['exchange'] = ex
    return exchange

if __name__ == '__main__':

    exs = ['bf', 'cc', 'bb', 'qx', 'zf']
    
    while True:
        exchanges = []
        ex_pairs  = []
        l_margins = []

        for ex in exs:
            exchanges.append(get_exchange(ex))

        for ex in itertools.combinations(exchanges, 2):
            margin = get_margin(ex[0], ex[1])
            l_margins.append(round(margin, 2))
            ex_pairs.append(ex[0]['exchange'] +'_' + ex[1]['exchange'])
            print(ex_pairs)

        now = datetime.now().strftime("%Y_%m_%d")
        filename = "margins/margins_" + now + ".csv"

        target_line = linecache.getline(filename, 1)
        inlines = target_line.split(',')
        print(len(inlines))
        if inlines[0].replace('.','').isnumeric() or len(inlines) < 2:
            if not(os.path.isfile(filename)):
                with open(filename, mode='w') as f:
                    f.write('')
            print('write ex_pairs in headline')
            with open(filename, mode='r+') as f:
                f.write(','.join(list(map(str, ex_pairs)))+'\n')

        margins = ','.join(list(map(str, l_margins)))
        print(margins)
        #margins = str(180)
        #args = ["echo", margins, '>>', filename]
        cmd = "echo " + margins + " >> " + filename
        subprocess.run(cmd, shell=True)
        time.sleep(interval)




