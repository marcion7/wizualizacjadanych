import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1, 20)

plt.plot(x, 1/x, label='f(x) = 1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.title("Wykres funkcji f(x) = 1/x dla x [1,20]")

plt.legend()

plt.show()