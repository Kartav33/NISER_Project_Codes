from cmath import e
import math
from tokenize import Double 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pan
import random
from scipy.interpolate import make_interp_spline
from scipy.spatial import ConvexHull
import mpl_toolkits.mplot3d 
import matplotlib

'Plotting the theoretical data'
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

plt.plot(X_,Y_,color='pink',label='$D_0$')

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

plt.plot(X_,Y_,color='m',label='$D_1$')

'Now,writing the Rk4 algorithm'

x0p=0;y0=1;z0=0;h1=0.0001;t=3


def f(x0,y0,z0,n):
    z=-x0*x0*pow(y0,n);
    return z

def g(x0,y0,z0):
    return z0/pow(x0,2)

n=0.5
xaxis=[];yaxis=[]
h = h1/10;
x0= x0p+ 0.00001;
k1=0;l1=0;k2=0;l2=0;l3=0;l4=0;k3=0;k4=0;y0=1;z0=0;c=0
while (x0 < t):
    k1 = h * g (x0, y0, z0);
    l1 = h * f (x0, y0, z0, n);

    k2 = h * g (x0 + (h/2), y0 + (k1/2), z0 +(l1/2));
    l2 = h * f (x0 + (h/2), y0 + (k1/2), z0 +(l1/2), n);

    k3 = h * g (x0 + (h/2), y0 + (k2/2), z0 +(l2/2));
    l3 = h * f (x0 + (h/2), y0 + (k2/2), z0 +(l2/2), n);

    k4 = h * g (x0 + (h/2), y0 + (k3), z0 +(l3));
    l4 = h * f (x0 + (h/2), y0 + (k3), z0 +(l3), n);

    y1 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    z1 = z0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6;
    y0 = y1;
    z0 = z1;

    xaxis.append(x0);
    yaxis.append(y0);
    x0 = x0 + h;
    if y0 < 0:
        break;  


plt.plot(xaxis,yaxis,label='$D_1$ using Rk4')
plt.xlabel('\u03BE')
plt.ylabel('$D_n(\u03BE)$')
plt.ylim(0,1.1)
plt.xlim(0,5)
plt.title('Interpolation of n=0.5')
#plt.show()

"Creating the inverse function list for performing the Interpolation"
y=0.00
X0p=[];X1p=[];Y0=[]
for item in range(1,101):
    X0=math.sqrt(6-6*y)
    X0p.append(X0)
    Y0.append(y)
    y=y+0.01

y1=0.00
Y1=[]
for item in range(1,101):
    x=0.0001
    for item in range(1,30000):
        if y1 <= (math.sin(x))/x <= y1 + 0.0001:
            X1p.append(x)
            Y1.append(y1)
            break
        x=x+0.0001
    y1=y1+0.01

y5=0.01
X5p=[]; Y5=[]
for item in range(1,101):
    X5=pow(3/(y5*y5)-3,0.5)
    #X5=math.sqrt(6-6*y3)
    X5p.append(X5)
    Y5.append(y5)
    y5=y5+0.01

'Taking Intersection'

YM=[];X0n=[];X1n=[];X5n=[]

N=0
for item in range(1,96):
    M=0
    for item in range(1,101):
        if Y0[M]==Y1[N]:
            YM.append(Y0[M])
            X0n.append(X0p[M])
            X1n.append(X1p[N])
        M=M+1
    N=N+1

N=0
for item in range(1,96):
    M=0
    for item in range(1,100):
        if YM[N]==Y5[M]:
            X5n.append(X5p[M])
        M=M+1
    N=N+1

'Now, we have four lists with 95 elements each YM, X0n, X1n, X5n'
'Linear interpolation using indices 0 and 1'

t=0
Xitpld1=[]
for item in range(1,96):
    Xin=(X1n[t]+X0n[t])/2   #Linear intepolation equation for n=0.5
    Xitpld1.append(Xin)
    t=t+1

plt.scatter(Xitpld1,YM,color='red',s=0.6, label='Linear Int.') 


'Quadratic interpolation Algorithm using the known three indices 0, 1 , and 5'

Xitpld=[];Yitpld=[]

i=0
for item in range(1,96):
    b0=0
    b1=1/(X1n[i]-X0n[i])
    b2=(5/(X5n[i]-X0n[i])-1/(X1n[i]-X0n[i]))/(X5n[i]-X1n[i])
    a=b2
    b=b1 - b2*(X0n[i]+X1n[i])
    c=b0 - n - b1*X0n[i] + b2*X0n[i]*X1n[i]
    D=b*b - 4*a*c
    if D >= 0:
        root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        if X0n[i] <= root1 <= X5n[i]:
            Xin=root1
        else:
            Xin=root2
        Xitpld.append(Xin)
        Yitpld.append(YM[i])
    i=i+1


plt.scatter(Xitpld,Yitpld,color='green',s=0.8, label='Qudratic int.')


plt.legend(scatterpoints=1, frameon=True, labelspacing=1)
matplotlib.rcParams['legend.fontsize'] = 50

plt.grid()
plt.show()