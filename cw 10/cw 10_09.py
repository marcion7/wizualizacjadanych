import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',sep=';')

wykres = df.groupby(df['Sprzedawca']).agg({'Utarg':['sum']}).reset_index()

wykres.columns = wykres.columns.droplevel(1)
a = wykres['Utarg']

plt.pie(a, labels=wykres['Sprzedawca'],autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color="black"),shadow=True,explode=(0.1,0.1,0,0.1,0,0,0.1,0.1,0))
plt.title("Udzial poszczegolnych sprzedawców w %")
plt.legend(title='Sprzedawcy')
plt.show()