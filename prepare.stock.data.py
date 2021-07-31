import pandas as pd
import numpy as np

def fill_next_line(df, start_index, next_index, line):
  next_line = df.iloc[start_index + next_index]
  for label in next_line.index:
    if label != 'ts_code' and label != 'trade_date':
      line[label+'_'+str(next_index)] = next_line[label]

def prepare_data(ts_code):
  result = pd.DataFrame({})

  df = pd.read_csv('finance/daily_price/'+ts_code)

  num_labels = ['open','high','low','close','pre_close','change','vol','amount']
  for label in num_labels:
    df[label] = np.log(df[label])
  
  for index, line in df.iterrows():

    if index > df.index.size - 30:
      result.to_csv('finance/preprocess/'+ts_code, index=False)
      break

    for i in range(1, 30):
      fill_next_line(df, index, i, line)

    result = result.append(line)

prepare_data('000001.SZ')