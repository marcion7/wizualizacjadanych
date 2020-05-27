import numpy as np

def fibo(n):
    lista =[]
    m = 1
    p = 0
    for i in range(n):
        r = m + p
        lista.append(r)
        p = m
        m = r
    return lista


a = fibo(25)

a = np.array(a).reshape(5,5)

print(a)