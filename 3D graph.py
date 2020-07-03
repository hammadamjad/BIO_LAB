from mpl_toolkits.mplot3d import Axes3D
from mplot3d_dragger import Dragger3D
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()
lst_x = []
lst_z1 = []
lst_z2 = []
lst_z3 = []
J=0
e = 16887
while(J<6):
    lst_x.append(e)
    e += 16887
    J += 1
def func(lst_z,y):
    ex = 16887
    t = 0.1
    i = 0
    while(i<6):
        z1 = 0.0027038/(t*y*3.14*pow(0.0015,2))
        z2 = 1-pow(ex/101325,0.75187)
        z = z1*z2
        lst_z.append(z)
        ex+=16887
        i+=1
    return lst_z

x = lst_x
z1 = func(lst_z1,2)
z2 = func(lst_z2,5)
z3 = func(lst_z3,10)
plt.plot(x, z1,label = "NO. OF HOLES = 2", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.plot(x, z2,label = "NO. OF HOLES = 5", marker='o',markersize=12, markerfacecolor='black',color='red',linewidth=4)
plt.plot(x, z3,label = "NO. OF HOLES = 10", marker='o',markersize=12, markerfacecolor='black',color='blue',linewidth=4)
plt.xlabel('PRESSURE ')
plt.ylabel('VELOCITY')
plt.title("AIR EVACUATING VELOCITY")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
