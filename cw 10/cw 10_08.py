import numpy as np
import matplotlib.pyplot as plt
import random


def rzucaj(n):
    lista = []
    for n in range(n):
        lista.append(random.randint(1, 6)+random.randint(1, 6))
    return lista


# liczba rzutów
n = 1000

plt.hist(rzucaj(n), bins=50, facecolor='g', alpha=0.75, density=True)


plt.xlabel('Suma oczek')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')

plt.grid(True)
plt.show()