from autogluon.tabular import TabularDataset, TabularPredictor

data = TabularDataset('finance/prepare2.data')

label = 'five_change'

train_data = data[0:0].append(data[100:])
test_data = data[0:99]
drop_columns = ['pct_chg', 'open', 'high', 'low', 'pre_close', 'change', 'close', 'vol', 'amount', 'ts_code', 'trade_date', 'pct_chg_1', 'pct_chg_2', 'pct_chg_3', 'pct_chg_4', 'open_1', 'open_2', 'open_3', 'open_4', 'high_1', 'high_2', 'high_3', 'high_4', 'low_1', 'low_2', 'low_3', 'low_4', 'pre_close_1', 'pre_close_2', 'pre_close_3', 'pre_close_4', 'change_1', 'change_2', 'change_3', 'change_4', 'close_1', 'close_2', 'close_3', 'close_4', 'vol_1', 'vol_2', 'vol_3', 'vol_4', 'amount_1', 'amount_2', 'amount_3', 'amount_4']
# subsample_size = 1000  # subsample subset of data for faster demo, try setting this to much larger values
# train_data = train_data.sample(n=subsample_size, random_state=0)
# train_data.head()

print("Summary of class variable: \n", train_data[label].describe())

predictor = TabularPredictor(label=label).fit(
  train_data.drop(columns=drop_columns)
  # , presets='best_quality'
  )

y_test = test_data[label]  # values to predict
drop_columns_with_close = drop_columns.copy()
drop_columns_with_close.append(label)
test_data_nolab = test_data.drop(columns=drop_columns_with_close)
test_data_nolab.head()

y_pred = predictor.predict(test_data_nolab)
print("Predictions:  \n", y_pred)

feature = predictor.feature_importance(test_data.drop(columns=drop_columns))
print('feature importance', feature)
feature.to_csv('finance/feature_importance')

import pandas as pd 

result = pd.DataFrame({'trade_date': test_data['trade_date'], 'pre_close': test_data['pre_close'], 'real': test_data[label], label: y_pred })
result.to_csv('finance/result', index=False)

perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)



