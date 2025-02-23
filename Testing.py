import pandas as pd

df = pd.read_parquet('D:/Py/Stocks/1st feb rec30A/JAN.parquet')
#print(df)

df.to_csv('D:/Py/Stocks/1st feb rec30A/JAN.csv', index=False)