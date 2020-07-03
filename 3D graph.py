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
e = 120
while(J<9):
    lst_x.append(e)
    e += 10
    J += 1
def func1(lst_z,y):
    ex = 120
    t = 0.1
    i = 0
    while(i<9):
        tg = 387 +((-83.5*math.log10(1/y))/(32.58+math.log10(1/y)))
        z = 1337*((1.42*tg+44.7)/(1.27*tg+0.3*ex))
        lst_z.append(z)
        ex+=10
        i+=1
    return lst_z
def func2(lst_z,y):
    ex = 120
    t = 0.1
    i = 0
    while(i<9):
        tg = 354 +((54*math.log10(1/y))/(3.4+math.log10(1/y)))
        z = 1060*((1.42*tg+44.7)/(1.27*tg+0.3*ex))
        lst_z.append(z)
        ex+=10
        i+=1
    return lst_z

x = lst_x
z1 = func1(lst_z1,0.1)
z2 = func2(lst_z2,0.1)
# z3 = func(lst_z3,1)
# plt.plot(x, z1,label = "STRAIN RATE = 0.1", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.plot(x, z2,label = "STRAIN RATE = 0.1", marker='o',markersize=12, markerfacecolor='black',color='red',linewidth=4)
# plt.plot(x, z3,label = "NO. OF HOLES = 10", marker='o',markersize=12, markerfacecolor='black',color='blue',linewidth=4)
plt.xlabel('TEMPERATURE ')
plt.ylabel('DENSITY')
plt.title("DENSITY ANALYSIS")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
