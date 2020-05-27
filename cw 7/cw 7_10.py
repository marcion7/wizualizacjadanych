import numpy as np

a = np.arange(81).reshape(9,9)
print(a)

 # b = a.reshape(6,3)
 # nie zadziała bo można zmienić kształt tylko jeżeli iloczyny są równe.

b = a.reshape(27,3)
print(b)
