from mpl_toolkits.mplot3d import Axes3D
from mplot3d_dragger import Dragger3D
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()

lst_z1 = []
lst_z2 = []
lst_z3 = []

def func(lst_z,y):
    ex = 80
    i = 0
    while(i<8):
        C1 = (0.0003768*pow(ex,2))-(0.128*ex)-0.876
        C2 = (0.00007053* pow(ex, 2)) + (0.018* ex) + 1.199
        z1 = 2*C1*(y-(1/pow(y,4)))
        z2 = 2*C2*(pow(y,3)-(1/pow(y,2)))
        z = z1+z2
        lst_z.append(z)
        ex+=10
        i+=1
    return lst_z

x = [80,90,100,110,120,130,140,150]
z1 = func(lst_z1,1.8)
z2 = func(lst_z2,2)
z3 = func(lst_z3,2.4)
plt.plot(x, z1,label = "STRETCH RATIO = 1.8", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.plot(x, z2,label = "STRETCH RATIO = 2", marker='o',markersize=12, markerfacecolor='black',color='red',linewidth=4)
plt.plot(x, z3,label = "STRETCH RATIO = 2.4", marker='o',markersize=12, markerfacecolor='black',color='blue',linewidth=4)
plt.xlabel('TEMPERATURE')
plt.ylabel('TRUE STRESS')
plt.title("STRESS ANALYSIS")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
