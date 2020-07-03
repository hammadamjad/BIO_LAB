import math
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
e = 15
while(J<10):
    lst_x.append(e)
    e += 2
    J += 1
def func(lst_z,):
    ex = 15
    i = 0
    while(i<10):
        z = pow(1+0.64*0.0000012345*(pow(ex/100,2)/pow(1-(ex/100),2)),-0.5)
        lst_z.append(z)
        ex+=2
        i+=1
    return lst_z

x = lst_x
z1 = func(lst_z1)
plt.plot(x, z1,label = "DEPTH OF MOLD = 80mm", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.xlabel('RADIUS OF PLUG (rp)')
plt.ylabel('STRETCH RATIO')
plt.title("STRETCH ANALYSIS")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
