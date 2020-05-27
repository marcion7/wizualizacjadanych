import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

dzieci = df.groupby(df['Rok']).agg({'Liczba':['sum']})
dzieci.plot()
plt.title('Liczba urodzonych dzieci w danym roku')
plt.xlabel('Lata')
plt.ylabel('Liczba urodzeń')
plt.legend()
plt.legend().get_texts()[0].set_text('Liczba urodzeń')
plt.show()