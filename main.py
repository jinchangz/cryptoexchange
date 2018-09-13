#import api_key
import ccxt
import io
from pprint import pprint
import time
import json

freq = 5

if __name__ == '__main__':



    bf = ccxt.bitflyer()
    # ticker = bitflyer.fetch_ticker('BTC/JPY', params = { "product_code" : "FX_BTC_JPY" })
    bf_ticker = bf.fetch_ticker('BTC/JPY')
    with open('tickers/bf_ticker.json', 'w') as f:
        json.dump(bf_ticker, f, indent=2, ensure_ascii=False)
    print('bitflyer_info-------------------------------' + str(type(bf_ticker)))

    pprint(bf_ticker)

    cc = ccxt.coincheck()
    cc_ticker = cc.fetch_ticker('BTC/JPY')
    print('coincheck_info------------------------------' + str(type(cc_ticker)))
    pprint(cc_ticker)

    

    
    #while True: