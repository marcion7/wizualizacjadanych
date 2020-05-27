import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')

wykres = df.groupby(df['Plec']).agg({'Liczba':['sum']})
wykres.plot.bar()
plt.title('Liczba urodzonych chłopców i dziewczynek')
plt.ylabel('Liczba urodzeń')
plt.legend()
plt.legend().get_texts()[0].set_text('Liczba urodzeń')
plt.show()
