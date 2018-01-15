from coinmarketcap import Market
import sys

DB = 'coins.txt'

try:
    while True:
        coinmarketcap = Market()
        
        with open(DB, 'a+') as f:
            coins = [x.strip('\n') for x in f.readlines()]
            
            for coin in coins:
                name = coin.split(' ')[0:-1][0]
                quant = int(coin.split(' ')[-1])
                price = float(coinmarketcap.ticker(currency=name)[0]['price_usd'])
                print name + ': $' + str(price) +' * ' + str(quant) + ' = $' + str(quant * price)
        print

        cur = raw_input()
        if len(cur):
            if cur[0] == '+':
                with open(DB, 'a+') as f:
                    f.write(cur.split(' ')[0:-1][0][1:] + ' ' + cur.split(' ')[-1] + '\n')
                    print cur[1:] + ' added succesfully.\n'
            elif cur[0] == '-':
                with open(DB, 'r+') as f:
                    coindb = f.readlines()

                    for idx, coin in enumerate(coindb):
                        if cur[1:] in coindb[idx]:
                            del coindb[idx]
                            break

                    f.seek(0)
                    
                    for entry in coindb:
                        f.write(entry)
                 
                    f.truncate()
            else:
                print "Value (USD): " + coinmarketcap.ticker(currency=cur)[0]['price_usd']
except KeyboardInterrupt:
    pass