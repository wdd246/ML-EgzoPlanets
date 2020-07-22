import pandas as pd

train = pd.read_csv('exoTrain.csv')
test = pd.read_csv('exoTest.csv')

print('Dane treningowe\n', train.head())
print('Dane testowe\n', test.head())

