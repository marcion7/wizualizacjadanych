import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)

s = np.sin(x)
c= np.cos(x)

plt.subplot(1,2,1)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.annotate('punkt(0,0)', xy=(0, 0), xytext=(-1.5,-0.15),arrowprops=dict(arrowstyle='-|>',color='black'))
plt.annotate('największa wartość', xy=(7.9, 1), xytext=(10,1.2),arrowprops=dict(arrowstyle='->', color='red', linewidth=2))
plt.annotate('najmniejsza wartość', xy=(17.3, -1), xytext=(18,-1.3),arrowprops=dict(arrowstyle='fancy', color='blue', linewidth=3))

plt.xlabel('x')
plt.ylabel('y')

plt.title("Wykres sin(x) i cos(x))")

plt.legend()

x = np.linspace(1, 20)

plt.subplot(1,2,2)
plt.plot(x, 1/x, label='f(x) = 1/x')
plt.annotate('wartość dla x=5', xy=(5, 0.2), xytext=(2,0.1),arrowprops=dict(arrowstyle='-',color='lime'))
plt.annotate('największa wartość', xy=(1, 1), xytext=(10,1.02),arrowprops=dict(arrowstyle='-|>', color='green', linewidth=4))


plt.xlabel('x')
plt.ylabel('f(x)')

plt.title("Wykres funkcji f(x) = 1/x dla x [1,20]")

plt.legend()

plt.show()