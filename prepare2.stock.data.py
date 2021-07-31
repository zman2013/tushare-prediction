# 算最近5天的振幅
import pandas as pd

ts_code = '000001.SZ'

df = pd.read_csv('finance/preprocess/'+ts_code)

df['five_change'] = -1
df.loc[df['close'] > df['close_4'], 'five_change'] = 1

df.to_csv('finance/prepare2.data', index=False)


drop_columns = ['pct_chg','open','high','low','pre_close','change','close','vol','amount']
columns = drop_columns.copy()
columns.append('ts_code')
columns.append('trade_date')
for column in drop_columns:
  for i in range(1,5):
    columns.append(column+'_'+str(i))

print(columns)    