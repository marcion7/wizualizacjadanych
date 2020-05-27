import numpy as np

def potegi(n,m):
    
    m = (np.logspace(1,m,num=m,base=n,dtype='int64'))
    return m

print(potegi(4,5))
