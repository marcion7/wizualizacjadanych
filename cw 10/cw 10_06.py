import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import openpyxl


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

wykres = (df.groupby(df['Plec']).agg({'Liczba':['sum']}).reset_index())

wykres.columns = wykres.columns.droplevel(1)
a = wykres['Liczba']

dzieci = (df.groupby(df['Rok']).agg({'Liczba':['sum']}).reset_index())

dzieci.columns = dzieci.columns.droplevel(1)
b = dzieci['Liczba']

chlopcy = (df.where(df['Plec'] == 'M').groupby(df['Rok']).agg({'Liczba':['sum']}).reset_index())
dziewczynki = (df.where(df['Plec'] == 'K').groupby(df['Rok']).agg({'Liczba':['sum']}).reset_index())

chlopcy.columns = chlopcy.columns.droplevel(1)
dziewczynki.columns = dziewczynki.columns.droplevel(1)

c = chlopcy['Liczba']
d = dziewczynki['Liczba']


plt.subplot(3,1,1)
plt.subplots_adjust(hspace=0.7)
plt.bar(wykres['Plec'],a)
plt.title('Liczba urodzonych chłopców i dziewczynek')
plt.ylabel('Liczba urodzeń')


plt.subplot(3,1,2)
plt.plot(chlopcy['Rok'],c,color='red',label='chlopcy')
plt.plot(dziewczynki['Rok'],d,color='pink',label='dziewczynki')
plt.title('Liczba urodzonych chłopców i dziewczynek w danym roku')
plt.xlabel('Lata')
plt.ylabel('Liczba urodzeń')
plt.legend()

plt.subplot(3,1,3)
plt.bar(dzieci['Rok'],b,color='green')
plt.title('Liczba urodzonych dzieci w danym roku')
plt.xlabel('Lata')
plt.ylabel('Liczba urodzeń')




plt.show()