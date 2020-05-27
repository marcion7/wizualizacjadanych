import numpy as np

def lista(n):
    lista = []
    for i in range(n):
        
        lista.extend(np.arange(2*n,2,-2))
        lista.extend(np.arange(2,2*n+1,2))
    
    s = lista[n-1:n-1+n]

    p = 1
    k = -3 + n
    for i in range(n-1):
        s.extend(lista[n+n*p+k:n+n+n*p+k])
        p += 1
        k += n-2
    s = np.array(s).reshape(n,n)
    return s

print(lista(3))