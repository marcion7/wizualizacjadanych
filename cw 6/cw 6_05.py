import numpy as np

def diag(n):
    
    m = np.diag(np.arange(n,0,-1))
    return m

print(diag(3))
