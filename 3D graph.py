from mpl_toolkits.mplot3d import Axes3D
from mplot3d_dragger import Dragger3D
import numpy as np
import matplotlib.pyplot as plt

lst_y = []
lst_n = []

fig = plt.figure()
ax = Axes3D(fig)

def f(x, y):
    E1 = np.exp(2*y)+(2*np.exp(-y))
    E2 = np.exp(-2*y)+(2*np.exp(y))
    # expo = -N/(E2*0.1)
    z = (0.00967*(E1-3))+(0.00244 *(E2-3))
    return z

# ex = 110
# g = 12
# t = 1
# E = 250
# i=0
# while(i<10):
#     n = 575+(6.325*ex)-(0.0175*pow(ex,2))
#     ey = (g/E)*(1-np.exp(-E/(n*t)))
#     lst_y.append(ey)
#     lst_n.append(n)
#     ex+=10
#     g+=2
#     t+=1000
#     E+=40
#     i+=1
# len_y = len(lst_y)-1
# len_n = len(lst_n)-1
x = np.linspace(120, 200, 30)
y = np.linspace(0.1,2.5, 30)
# N = np.linspace(lst_n[0],lst_n[len_n],30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
ax.set_title('STRAIN ENERGY ANALYSIS')
surf1 = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
fig.colorbar(surf1, ax=ax, shrink=0.5, aspect=5)
ax.set_xlabel("TEMPERATURE")
ax.set_ylabel("STRAIN")
ax.set_zlabel("STRAIN ENERGY")
dr = Dragger3D(ax)
plt.show()
