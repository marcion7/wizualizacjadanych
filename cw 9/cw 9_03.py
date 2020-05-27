import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')


wykres = df.where((df['Rok'] <= 2017) & (df['Rok'] >= 2013)).groupby(df['Plec']).agg({'Liczba':['sum']})
wykres.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('Dzieci urodzone w latach 2013-2017 w %')
plt.ylabel('')
plt.xlabel('Płeć')
plt.legend()
plt.show()
