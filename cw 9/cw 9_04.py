import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

wykres = pd.DataFrame(df)

grupy = wykres.groupby('species')

for nazwa, grupa in grupy:
    plt.plot(grupa["petal_length"], grupa["petal_width"], marker="o", linestyle="", label=nazwa)

plt.title('Porównianie długości płatka i szerokości płatka w poszczególnych gatunkach')
plt.xlabel('Długość płatka')
plt.ylabel('Szerokość płatka')
plt.legend()

plt.show()