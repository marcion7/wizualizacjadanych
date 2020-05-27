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

# szerokość 2 razy większa niż wysokość
fig = plt.figure( figsize =plt.figaspect( 0.5 ))
#===============
# Pierwszy wykres
#===============
ax = fig.add_subplot( 1 , 2 , 1 , projection = '3d' )
ax.scatter(losuj(20),losuj(20),losuj(20), marker ='o')
#===============
# Drugi wykres
#===============
ax = fig.add_subplot( 1 , 2 , 2 , projection = '3d' )
z = np.linspace(1,99999,5)
ax.plot(losuj(5),losuj(5),z)
plt.show()
