import numpy as np
import matplotlib.pyplot as plt

c = np.array( [5,8,23,54,35.5,24.3] ).reshape(2,3)

a = np.sin(c)

d = np.array( [96,3,56,25,67.69,45.41] ).reshape(2,3)

b = np.cos(d)

print(np.add(a,b))
