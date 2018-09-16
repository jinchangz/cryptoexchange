import sys
import time
import ccxt
import json
import os

print('shell start')
interval = 1
ex = ccxt.coincheck()
ex_name = 'cc'
filename = os.path.normpath(os.path.join(os.path.abspath(__name__),'../tickers/' + ex_name + '_ticker.json'))

try:
    while True:

        ex_json = ex.fetch_ticker('BTC/JPY')

        with open(filename, 'w') as f:
            json.dump(ex_json, f, indent=2, ensure_ascii=False)
        time.sleep(interval)
except:
    print('through any exception. exit get_' + ex_name + '_ticker.py')
    sys.exit()
