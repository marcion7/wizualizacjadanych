import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',sep=';',parse_dates=True)


wykres = df.groupby(df['Sprzedawca']).agg({'idZamowienia':['count']})
wykres.plot.bar()
plt.title('Ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.ylabel('Ilość złożonych zamówień')
plt.legend()
plt.legend().get_texts()[0].set_text('Ilość zamówień')
plt.show()
