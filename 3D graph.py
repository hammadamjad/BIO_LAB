import math
from mpl_toolkits.mplot3d import Axes3D
from mplot3d_dragger import Dragger3D
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()
lst_x = []
lst_z1 = []
J=0
e = 0
while(J<10):
    H = e/254
    lst_x.append(H)
    e += 16
    J += 1
def func(lst_z,):
    ex = 0
    i = 0
    while(i<10):
        num = (508*ex)/(64516+pow(ex,2))
        dem = np.arcsin(num)
        z = num/dem
        lst_z.append(z)
        ex+=16
        i+=1
    return lst_z

x = lst_x
z1 = func(lst_z1)
plt.plot(x, z1,label = "HALF WIDTH = 254mm", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.xlabel('H/a')
plt.ylabel('t/to')
plt.title("THICKNESS VARIATION")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
