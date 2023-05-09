import pandas as pd

data = pd.read_csv('gruppa.csv', delimiter=";")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
print(data)

print("----------------------------------------------------------")

print(data.sort_values (by='Дата рождения (год, месяц и число)'))