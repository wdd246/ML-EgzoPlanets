import pandas as pd

train = pd.read_csv('exoTrain.csv')
test = pd.read_csv('exoTest.csv')

print('Dane treningowe\n', train.head())
print('Dane testowe\n', test.head())

x_train = train.drop('LABEL', axis=1)
y_train = train.LABEL-1
x_test = test.drop('LABEL', axis=1)
y_test = test.LABEL-1

# MODEL TFBT

#numeric_column_headers = x_train.columns.values.tolist()

#bc_fn = tf