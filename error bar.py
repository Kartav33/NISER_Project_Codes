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

'Now, writing the Rk4 algorithm'

x0p=0;y0=1;z0=0;h1=0.0001;t=10

def f(x0,y0,z0,n):
    z=-x0*x0*pow(y0,n);
    return z

def g(x0,y0,z0):
    return z0/pow(x0,2)

n=3
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


plt.plot(xaxis,yaxis,color='yellow', label='$D_3$ using Rk4')
plt.xlabel('\u03BE')
plt.ylabel('$D_n(\u03BE)$')
plt.xlim(0,5)
plt.ylim(0,1.1)
plt.title('Error due to linear interpolation of n=3')
#plt.show()

'Writng the Rk4 algorithm again but this time as a customized function with variable input values'
def rk4(t):
    x0p=0;y0=1;z0=0;h1=0.0001

    def f(x0,y0,z0,n):
        z=-x0*x0*pow(y0,n);
        return z

    def g(x0,y0,z0):
        return z0/pow(x0,2)

    n=3
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

        x0 = x0 + h;
        if y0 < 0:
            break;
    return y0


"Creating the inverse function list for performing the Interpolation"
y=0.00
X0p=[];Y0=[]
for item in range(1,101):
    X0=math.sqrt(6-6*y)
    X0p.append(X0)
    Y0.append(y)
    y=y+0.01

y2=0.00
X1p=[];Y1=[]
for item in range(1,101):
    x=0.0001
    for item in range(1,30000):
        if y2 <= (math.sin(x))/x <= y2 + 0.0001:
            X1p.append(x)
            Y1.append(y2)
            break
        x=x+0.0001
    y2=y2+0.01

y3=0.01
X5p=[]; Y5=[]
for item in range(1,100):
    X5=pow(3/(y3*y3)-3,0.5)
    #X5=math.sqrt(6-6*y3)
    X5p.append(X5)
    Y5.append(y3)
    y3=y3+0.01


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
'Linear interpolation using indices 0 and 5'
t=0
Xitpld1=[];Xitpld3=[]
for item in range(1,96):
    Xin1=(3*X5n[t]+2*X0n[t])/5   #Linear intepolation equation for n=3 using 0 and 5
    Xin3=(X5n[t]+X0n[t])/2      #Linear intepolation equation for n=3 using 1 and 5
    Xitpld1.append(Xin1)
    Xitpld3.append(Xin3)
    t=t+1

#plt.scatter(Xitpld1,YM,color='red',s=0.2, label='Linear Int. using 0 and 5') 
#plt.scatter(Xitpld3,YM,color='pink',s=0.2, label='Linear Int. using 1 and 5') 

'Calculating the error bar of linear interpolation'
'case 1: when 0 and 5 are used'
lerr1=[];i=0; Yr1=[];YP1=[]
for item in Xitpld1:
    yrk=rk4(Xitpld1[i])
    Yr1.append(yrk)
    yer=abs(YM[i]-yrk)
    YP1.append(yer*100)
    lerr1.append(yer)
    i=i+1

'case 2: when 1 and 5 are used'
lerr3=[];i=0; Yr3=[];YP3=[]
for item in Xitpld3:
    yrk=rk4(Xitpld3[i])
    Yr3.append(yrk)
    yer=abs(YM[i]-yrk)
    YP3.append(yer*100)
    lerr3.append(yer)
    i=i+1

#plt.scatter(Xitpld1,Yr1,color='b')
#plt.errorbar(Xitpld1,Yr1,lerr1, label='error due linear int. using 0 and 5',fmt='orange',ls=None)
#plt.errorbar(Xitpld3,Yr3,lerr3, label='error due linear int. using 1 and 5',fmt='black',ls=None)

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

'Calculating the error bar of quadratic interpolation'
lerr2=[];i=0; Yr2=[];YP2=[]
for item in Xitpld:
    yrk=rk4(Xitpld[i])
    Yr2.append(yrk)
    yer=abs(yrk-YM[i])
    lerr2.append(yer)
    YP2.append(yer*100)
    i=i+1

#plt.scatter(Xitpld,Yitpld,color='green',s=0.7, label='Qudratic int.')


#plt.errorbar(Xitpld,Yr2,lerr2, label='error due quadratic int.',fmt='g',ls='none')
plt.legend(scatterpoints=1, frameon=True, labelspacing=1)
matplotlib.rcParams['legend.fontsize'] = 50

plt.grid()
plt.show()
#print(Xitpld)rint(Xitpld1)

'printing the error bar percentages'
#print('maximum percentage error due to linear interpolation when 0 and 5 are used ', max(YP1))
#print('\nminimum percentage error due to linear interpolation when 0 and 5 are used', min(YP1))
#print('maximum percentage error due to linear interpolation when 1 and 5 are used ', max(YP3))
#print('\nminimum percentage error due to linear interpolation when 1 and 5 are used', min(YP3))
#print('\nmaximum percentage error due to quadratic interpolation ', max(YP2))
#print('\nminimum percentage error due to quadratic interpolation ', min(YP2))

plt.plot(YM,YP1, label='Linear int. using 0 and 5')
plt.plot(YM,YP3, label='Linear int. using 1 and 5')
plt.plot(YM,YP2, label='Quadratic int.')
plt.title('Error Vs. $D_3$')
plt.xlabel('$D_3$')
plt.ylabel('Error percentage')
#plt.legend(scatterpoints=1, frameon=True, labelspacing=1)
#matplotlib.rcParams['legend.fontsize'] = 0.5
plt.legend(prop={'size':15})

plt.grid()
plt.show()