import pandas as pd
import pandas_ta as ta

dt = pd.read_csv("D:/Py/NIFTY.csv")

dt['SMA'] = ta.sma(dt['Close '],length=21)


entryprice = 0
stoploss = 0
isintrade = False
total = 0

for i in range (len(dt['Close '])):
    if (dt['Date '][i]=='27-Mar-24'):
        for count in range(i, len(dt['Close '])):
            #Stoploss
            if(dt['Close '][count] < dt['SMA'][count] and dt['Close '][count-1] > dt['SMA'][count-1] and isintrade == True):
                print('Down Crossover Detected / Exit Trade', dt['Date '][count])
                pnl = dt['Close '][count] - entryprice
                total = total + pnl
                isintrade = False
                print('Profit/Loss:', pnl, '\n')

            #Entry
            if(dt['Close '][count] > dt['SMA'][count] and dt['Close '][count-1] < dt['SMA'][count-1] and isintrade == False):
                print('Crossover Detected / Entry Trade Executed',dt['Date '][count])
                entryprice = dt['Close '][count]
                isintrade = True



print("Total profit or loss is: ", total)