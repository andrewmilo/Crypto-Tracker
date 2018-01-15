from coinmarketcap import Market
import sys

try:
    while True:
        coinmarketcap = Market()
        cur = raw_input()
        print coinmarketcap.ticker(currency=cur)[0]['price_usd']
except KeyboardInterrupt:
    pass