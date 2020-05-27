import numpy as np

a = np.arange(3,27,2)
print(a)

print('----------------------')

b = a.reshape(3,4)
print(b)

print('----------------------')

c = a.reshape(4,3)
print(c)

print('----------------------')

d = a.reshape(2,6)
print(d)

print('----------------------')

e = b.ravel()
print(e)

print('----------------------')

f = c.ravel()
print(e)

print('----------------------')

g = d.ravel()
print(e)

print('----------------------')

# Są identyczne





