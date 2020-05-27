import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)

s = -np.sin(x)
c= -np.cos(x)

s2 = np.sin(x)+2
c2 = np.cos(x)+2

plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.plot(x, s2, label='sin(x2)')
plt.plot(x, c2, label='cos(x2)')

plt.xlabel('x')
plt.ylabel('y')

plt.title("Wykres sin(x),sin(x2),cos(x),cos(x2)")

plt.legend()

plt.show()