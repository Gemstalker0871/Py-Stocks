import pandas as pd
import pandas_ta as ta

dt = pd.read_csv("D:/Py/NIFTY.csv")




print("done")

dt['SMA'] = ta.sma(dt['Close '],length=21)

print (dt.head(25))
dt.to_csv("niftytest.csv")