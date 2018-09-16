
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

def get_exchange(ex):
    with open('tickers/'+ ex + '_ticker.json') as f:
        exchange = json.load(f)
        exchange['exchange'] = ex
    return exchange['last']

if __name__ == '__main__':

    exs = ['bf', 'cc', 'bb', 'qx', 'zf']

    while True:
        exchanges = []

        for ex in exs:
            exchanges.append(get_exchange(ex))

        today = datetime.now().strftime("%Y_%m_%d")
        filename = "prices/prices_" + today + ".csv"

        target_line = linecache.getline(filename, 1)
        inlines = target_line.split(',')
        # print(len(inlines))
        if inlines[0].replace('.','').isnumeric() or len(inlines) < 2:
            if not(os.path.isfile(filename)):
                with open(filename, mode='w') as f:
                    f.write('')
            print('write ex_pairs in headline')
            with open(filename, mode='r+') as f:
                f.write(','.join(list(map(str, exs)))+'\n')

        prices = ','.join(list(map(str, exchanges)))
        # print(prices)

        cmd = "echo " + prices + " >> " + filename
        subprocess.run(cmd, shell=True)
        time.sleep(interval)




