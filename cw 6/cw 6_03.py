import numpy as np

def tablica(n):
    m = np.array((np.arange(1,n*n+1,1)).reshape((n,n)))
    return m

print(tablica(10))
