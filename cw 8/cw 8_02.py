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

grupa = df.groupby(['Rok'])
for i in range(2000,2018):
    print(df.where((df['Rok'] == i) & (df['Plec'] == 'M')).nlargest(1,'Liczba'))
    print(df.where((df['Rok'] == i) & (df['Plec'] == 'K')).nlargest(1,'Liczba'))
    i+=1

print('--------------------------------------')

print(df.where(df['Plec'] == 'M').nlargest(1,'Liczba'))
print(df.where(df['Plec'] == 'K').nlargest(1,'Liczba'))