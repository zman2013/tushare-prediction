import tushare
import pandas as pd
import time

print(tushare.__version__)

pro = tushare.pro_api('')

df = pd.read_csv('finance/all.stocks.basic.info.csv')
# 直接遍历line
for index, line in df.iterrows():
  code = line['ts_code']
  daily_price = pro.daily(ts_code=code, start_date='20070701')
  daily_price.to_csv('finance/daily_price/'+code, index=False)
  time.sleep(0.2)

print('finished')