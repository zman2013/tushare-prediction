import tushare

print(tushare.__version__)

pro = tushare.pro_api('')

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

data.to_csv('finance/all.stocks.csv', index=False)