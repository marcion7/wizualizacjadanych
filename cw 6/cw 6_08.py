import numpy as np


def podziel(tablica,kierunek):
    
    try:
        if kierunek == 'poziomo':
           s = np.vsplit(tablica,2)
           return s
        elif kierunek == 'pionowo':
           s = np.hsplit(tablica,2)
           return s
    except ValueError:
        return 'Nie mozna podzielic tablicy, wymiar musi być podzielny przez 2'
 


a = np.arange(110).reshape(10,11)
b = podziel(a,'poziomo')
print(b)