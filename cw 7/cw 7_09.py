import numpy as np

b = np.arange(9,27,2).reshape(3,3)
print(b)
for a in b.flat:

   print(a)