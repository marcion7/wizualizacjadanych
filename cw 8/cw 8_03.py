import pandas as pd
import numpy as np


df = pd.read_csv('zamowienia.csv',sep=';',parse_dates=True)

print(df['Sprzedawca'].unique())

print('--------------------------------------')

print(df['Utarg'].nlargest(5))

print('--------------------------------------')

print(df.groupby(["Sprzedawca"]).agg({'idZamowienia':['count']}))

print('--------------------------------------')

print(df.groupby(["Kraj"]).agg({'Utarg':['sum']}))

print('--------------------------------------')

df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
df['rok'] = df['Data zamowienia'].dt.year

print(df.where((df['Kraj'] == 'Polska') & (df['rok'] == 2005)).agg({'Utarg':['sum']}))

print('--------------------------------------')

print(df.where((df['rok'] == 2005)).agg({'Utarg':['mean']}))

print('--------------------------------------')

rok2004 = (df.where(df['rok'] == 2004).dropna())
rok2004.to_csv('zamowienia_2004.csv')

rok2005 = (df.where(df['rok'] == 2005).dropna())
rok2005.to_csv('zamowienia_2005.csv')

