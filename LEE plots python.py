from cmath import e, sin
import math 
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.interpolate import make_interp_spline
from scipy.spatial import ConvexHull

"defining some empty lists"
D0=[];D1=[];D5=[]
pt0=[];pt1=[];pt5=[]

"defining the functions for the polytropes at n=0, 1 and 5"
"n=0"
def func0(x):
    return 1-(x*x)/6

"n=1"
def func1(x):
    return math.sin(x)/x

"n=5"
def func5(x):
    e= 1/math.sqrt(1+(x*x)/3)
    return e

"Creating y-lists and x-lists"
"n=0"
x=0
for item in range(1,4000):
    D0.append(func0(x))
    pt0.append(x)
    x=x+0.001
    if func0(x) < 0:
        break

p=np.array(pt0)
q=np.array(D0)
X_Y_Spline= make_interp_spline(p,q)
X_ =np.linspace(p.min(),p.max(),500)
Y_ =X_Y_Spline(X_)

plt.plot(X_,Y_)

"n=1"
x=0.001
for item in range(2,4000):
    D1.append(func1(x))
    pt1.append(x)
    x=x+0.001
    if func1(x) < 0:
        break

p=np.array(pt1)
q=np.array(D1)
X_Y_Spline= make_interp_spline(p,q)
X_ =np.linspace(p.min(),p.max(),500)
Y_ =X_Y_Spline(X_)

plt.plot(X_,Y_)

"n=5"
x=0
for item in range(1,10000):
    D5.append(func5(x))
    pt5.append(x)
    x=x+0.001
    if func5(x) < 0:
        break

p=np.array(pt5)
q=np.array(D5)
X_Y_Spline= make_interp_spline(p,q)
X_ =np.linspace(p.min(),p.max(),500)
Y_ =X_Y_Spline(X_)

plt.plot(X_,Y_)

"Plotting the curves together with proper labels"
plt.xlim(0,10)
plt.xlabel('\u03BE')
plt.ylabel('$D_n(\u03BE)$')
plt.text(1.69,0.231,'$D_0$')
plt.text(2.51,0.257,'$D_1$')
plt.text(5.55,0.324,'$D_5$')
plt.grid()
plt.show()