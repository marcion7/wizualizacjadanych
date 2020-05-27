import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
# rejestrowanie projekcji 3d.
from mpl_toolkits.mplot3d import Axes3D


def losuj(n):
    lista = []
    for n in range(n):
        lista.append(np.random.randint(99999))
    return lista


fig = plt.figure()
#===============
# Pierwszy wykres
#===============
ax = fig.gca( projection = '3d' )
ax.scatter(losuj(20),losuj(20),losuj(20), marker ='o',color="red")
z = np.linspace(1,99999,5)
ax.plot(losuj(5),losuj(5),z,color="green")
plt.show()
