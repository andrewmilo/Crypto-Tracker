from coinmarketcap import Market
import sys

DB = 'coins.txt'

start_flag = True

try:
    while True:
        coinmarketcap = Market()
        
        if start_flag:
            with open(DB, 'r+') as f:
                coins = [x.strip('\n') for x in f.readlines()]
                
                for coin in coins:
                    print coin + ': $' + coinmarketcap.ticker(currency=coin)[0]['price_usd']
            start_flag = False
            print

        cur = raw_input('\nEnter Name and Quantity: ')
        # name = cur.split(' ')[0:-1][0]
        # quant = cur.split(' ')[-1]
        if len(cur):
            if cur[0] == '+':
                with open(DB, 'a+') as f:
                    f.write(cur[1:] + '\n')
                    print cur[1:] + ' added succesfully.'
            elif cur[0] == '-':
                with open(DB, 'r+') as f:
                    coindb = f.readlines()
                    if cur[1:]+'\n' in coindb:
                        coindb.remove(cur[1:]+'\n')
                    f.seek(0)
                    for entry in coindb:
                        f.write(entry)
                    f.truncate()
            else:
                print "Value (USD): " + coinmarketcap.ticker(currency=cur)[0]['price_usd']
        else:
            continue
except KeyboardInterrupt:
    pass