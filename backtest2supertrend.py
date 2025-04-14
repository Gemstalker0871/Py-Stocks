import pandas as pd
import pandas_ta as ta

df = pd.read_csv('D:/Py/Data/cleaned_combined_data.csv')

temp = ta.supertrend(high=df['High'], low = df['Low'], close=df['Close'], length=10, multiplier=3.0 )


df['ST_value'] = temp['SUPERT_10_3.0']
df['ST_trend'] = temp['SUPERTd_10_3.0'] 

#print(df)

df.to_csv('NiftySupertrend.csv',index=False)

entryprice=0
isintrade = False
total_pnl = 0

for i in range (len(df['Date'])):
    if(df['Date'][i]=='2022-01-21'):
        print("Backtesting started", df['Date'][i],'\n')
        for count in range (i,len(df['Date'])):
            if count > 0:
            
                #Stoploss
                if(df['ST_trend'][count]==-1 and df['ST_trend'][count-1]==1):
                    print("Trend Changed Red", df['Date'][count])
                    pnl = df['Close'][count] - entryprice
                    print("PnL",pnl,'\n')
                    total_pnl = pnl + total_pnl 
                    isintrade = False
                #entry
                if(df['ST_trend'][count]==1 and df['ST_trend'][count-1]==-1 and isintrade == False):
                    print("Trend Changed Green", df['Date'][count])
                    entryprice = df['Close'][count]
                    isintrade = True


if isintrade:
    print(f"End of dataset: Closing open position on {df['Date'][count]}")
    pnl = df['Close'][count] - entryprice
    print(f"Final PnL: {pnl:.2f}")
    total_pnl += pnl

print("Total pnl is", total_pnl)


#make dic of date entry, entry price, date exit, exit price, pnl