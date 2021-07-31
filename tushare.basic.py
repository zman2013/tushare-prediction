import tushare

print(tushare.__version__)

pro = tushare.pro_api('')

code = '000001.SH'

df = pro.daily(ts_code=code, start_date='20070701')

df.to_csv('finance/daily_price/'+code, index=False)

print(df)