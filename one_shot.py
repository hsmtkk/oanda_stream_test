import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

import util

accountID = util.get_env_var('OANDA_ACCOUNT')
accessToken = util.get_env_var('OANDA_TOKEN')
api = API(access_token=accessToken)
params ={"instruments": "USD_JPY"}

stream = pricing.PricingStream(accountID=accountID, params=params)
response = api.request(stream)
for ticks in response:
    print(ticks)
