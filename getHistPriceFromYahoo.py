import pandas as pd
import yfinance as yf

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
    print(symbol)
    sleep(1)
    ydata = yf.Ticker(symbol+'.NS')
    yhist = ydata.history(period='1y')
    yhist.to_csv(outdir + symbol + '.csv')

print( 'done.')
