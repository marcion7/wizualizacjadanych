import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

wykres = pd.DataFrame(df['sepal_length'])
wykres2 = pd.DataFrame(df['sepal_width'])
kolory = np.random.rand(len(wykres),3)
size= np.abs(df['sepal_length'] - df['sepal_width'])


plt.scatter(wykres,wykres2,c=kolory,s=size)

plt.title('Porównianie sepal_length i sepal_width')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.legend()

plt.show()