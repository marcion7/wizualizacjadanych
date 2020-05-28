import pandas as pd
import numpy as np

import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
df.to_excel('z_indeksami.xlsx',  sheet_name='Imiona z indeksami')


print(df[df['Liczba']>1000])

print('--------------------------------------')

print(df[df['Imie']=='MARCIN'])

print('--------------------------------------')

print(df.agg({'Liczba':['sum']}))

print('--------------------------------------')

print(df.where((df['Rok'] >= 2000) & (df['Rok'] <= 2005)).agg({'Liczba':['sum']}))

print('--------------------------------------')

print(df.groupby(df['Plec']).agg({'Liczba':['sum']}))

print('--------------------------------------')

dzieci = (df.where((df['Rok'] == 2000) & (df['Plec'] == 'M')).nlargest(1,'Liczba'))
df2 = (df.where((df['Rok'] == 2000) & (df['Plec'] == 'K')).nlargest(1,'Liczba'))
dzieci = pd.concat([dzieci,df2])
for i in range(2001,2018):
    dzieci1 = (df.where((df['Rok'] == i) & (df['Plec'] == 'M')).nlargest(1,'Liczba'))
    dzieci = pd.concat([dzieci,dzieci1])
    dzieci2 = (df.where((df['Rok'] == i) & (df['Plec'] == 'K')).nlargest(1,'Liczba'))
    dzieci = pd.concat([dzieci,dzieci2])

dziec = dzieci[['Rok','Imie']]
print(dziec)

print('--------------------------------------')

chl = (df.where(df['Plec'] == 'M').nlargest(1,'Liczba'))
dzi = (df.where(df['Plec'] == 'K').nlargest(1,'Liczba'))
chlopcy = chl[['Imie']]
dziewczynki = dzi[['Imie']]
print(chlopcy)
print(dziewczynki)
