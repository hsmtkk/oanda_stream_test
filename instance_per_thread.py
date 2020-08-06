import threading
import time

import oandapyV20
import oandapyV20.endpoints.pricing

import util

class APICaller(threading.Thread):
    def run(self):
        accountID = util.get_env_var('OANDA_ACCOUNT')
        accessToken = util.get_env_var('OANDA_TOKEN')
        api = oandapyV20.API(access_token=accessToken)
        params ={"instruments": "USD_JPY"}
        stream = oandapyV20.endpoints.pricing.PricingStream(accountID=accountID, params=params)
        response = api.request(stream)
        for ticks in response:
            print(ticks)

if __name__ == '__main__':
    while True:
        caller = APICaller()
        caller.start()
        time.sleep(1)
