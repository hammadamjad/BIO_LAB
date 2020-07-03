from mpl_toolkits.mplot3d import Axes3D
from mplot3d_dragger import Dragger3D
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()

lst_z = []
ex = 110
y=0.3
i=0
while(i<10):
    n = 575+(6.325*ex)-(0.0175*pow(ex,2))
    E1 = 65.1 - (0.6675 * ex) + (0.00175 * pow(ex, 2))
    E2 = 480 + (5.35 * ex) - (0.015 * pow(ex, 2))
    expo = -n / (E2 * 0.1)
    z = (E1 * y) + (E2 * 0.1) * (1 - np.exp(expo * y))
    lst_z.append(z)
    ex+=10
    y+=0.20
    i+=1

len_z = len(lst_z)-1
x = [110,120,130,140,150,160,170,180,190,200]
z = lst_z
plt.plot(x, z,label = "STRAIN RATE = 0.1", marker='o',markersize=12, markerfacecolor='black',color='orange',linewidth=4)
plt.xlabel('TEMPERATURE')
plt.ylabel('TRUE STRESS')
plt.title("STRESS ANALYSIS")
ax.set_facecolor('yellow')
plt.legend()
plt.show()
