import numpy as np

a = np.array([8,4,2,7,8,9,1,4,10]).reshape(3,3)
b = np.array([54,23,46,31,57,86,24,65,43,12,56,78,31,49,23,51]).reshape(4,4)

print(a)
print(a.min(axis=1))
print(a.min(axis=0))

print('-----------------------------')

print(b)
print(b.min(axis=1))
print(b.min(axis=0))



