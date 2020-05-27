import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import openpyxl


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')


chlopcy = (df.where(df['Plec'] == 'M').groupby(df['Rok']).agg({'Liczba':['sum']}).reset_index())
dziewczynki = (df.where(df['Plec'] == 'K').groupby(df['Rok']).agg({'Liczba':['sum']}).reset_index())

chlopcy.columns = chlopcy.columns.droplevel(1)
dziewczynki.columns = dziewczynki.columns.droplevel(1)

c = chlopcy['Liczba']
d = dziewczynki['Liczba']



plt.bar(chlopcy['Rok'],c,color='red',label='chlopcy')
plt.bar(dziewczynki['Rok'],d,color='blue',label='dziewczynki')
plt.title('Liczba urodzonych chłopców i dziewczynek w danym roku')
plt.xlabel('Lata')
plt.ylabel('Liczba urodzeń')
plt.legend()




plt.show()