import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 5

# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów

for c, m in [( 'red' , 'o' ), ( 'blue' , '^' ),( 'magenta' , 'v' ),( 'yellow' , '*' ),( 'green' , '+' )]:
    x = randrange(n, 0 , 99999 )
    y = randrange(n, 0 , 99999 )
    z = randrange(n, 0 , 99999 )
    ax.scatter(x,y,z, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()