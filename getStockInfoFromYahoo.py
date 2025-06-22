import pandas as pd
import yfinance as yf
import json

ddir = '/home/kray/DATA/nseindexconstituents/'
outdir = '/home/kray/DATA/yahoonsedata/'

dff = pd.read_table(ddir + 'nseindexconstituents.txt', header=None)
lfile = list(dff[0])


temp = []
for item in lfile:
    filename = ddir + item
    print (filename)

    df = pd.read_csv(filename)
    temp += list(df['Symbol'])

symbols = set(temp)

print( 'Num of symbols : ', len(symbols))


from time import sleep
sleep(10)


for symbol in symbols:
    yinfo = {}

    print(symbol + '-- info')
    sleep(1)
    try:
        
        ydata = yf.Ticker(symbol+'.NS')
    
        yinfo[symbol] = ydata.info
        with open(outdir + symbol + "-info.json", "w") as outfile:
            json.dump(yinfo, outfile, indent=4)
    except:
        print('not found')
                




print( 'done.')
