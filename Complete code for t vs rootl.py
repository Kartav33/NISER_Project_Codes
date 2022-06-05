from cmath import e
import math 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pan
import random
from scipy.interpolate import make_interp_spline
from scipy.spatial import ConvexHull
import mpl_toolkits.mplot3d 

"observed data sets"
time= [2.51,2.45,2.27,2.26,2.195,2.10,1.98]
rootl=[12.69,12.29,11.83,11.40,10.95,10.41,10.00]

"declaring empty lists"
xy=[];xsq=[]

"mean of observed data sets"
mtime=np.mean(time)
mrootl=np.mean(rootl)

"calculating the standard deviation/variance of our 7 data sets"
v=[]
for d in time:
    q=pow(d-mtime,2)
    v.append(q)
std=(sum(v)/7)

"calculation of regression coefficients"
for (x,y) in zip(time,rootl):
    a=y*y
    b=x*y
    xsq.append(a)
    xy.append(b)

b1=(sum(xy)-7*mtime*mrootl)/(sum(xsq)-7*pow(mrootl,2))
b0=mtime-mrootl*b1

etime=[]
for item in rootl:
    f=b0 + b1*item
    etime.append(f)

"To plot the best fit line, along with scatter points of our data sets and their individual errors"
"to plot the scatter points and the line together"
plt.scatter(rootl,time,color='red')
plt.ylabel("time")
plt.xlabel('√length')

plt.plot(rootl,etime)

"to calculate error bars and chisquare value"
s=[]
for (x,y) in zip(time,etime):
    b=(x-y)/(x-mtime)
    s.append(b*b)

p=[]
e1time=[]
for item in rootl:
    g=-0.25+0.22*item
    e1time.append(g)

t=[]                       #list to append individual errors
for x in time:
    b=x-mtime
    t.append(b/2)

for x,y in zip(e1time,time):
    b=pow(y-x,2)
    p.append(b/std)

plt.errorbar(rootl,time,yerr=t,ls='None')
plt.show()

"Likelihood Vs intercept plot using Spline functions"
a=-1
A=[];c=[]
for testa in range(1,201):
    chi=0
    c1=[]
    A.append(a)
    for (x,y) in zip(rootl,time):
        chi=(pow((y-a-(0.22*x)),2)/std)
        like=pow(e,-chi/2)
        c1.append(like)
    c.append(np.mean(c1))
    a=a+0.01

p=np.array(A)
q=np.array(c)
X_Y_Spline= make_interp_spline(p,q)
X_ =np.linspace(p.min(),p.max(),500)
Y_ =X_Y_Spline(X_)

plt.plot(X_,Y_)
plt.title('keeping slope constant')
plt.xlabel('\u03B1 (intercept)')
plt.ylabel('Likelihood function')
plt.show()

"Likelihood Vs slope plot using Spline functions"
b=0.1
B=[];d=[]
for testb in range(1,300):
    chi=0
    d1=[]
    B.append(b)
    for (x,y) in zip(rootl,time):
        chi=(pow((y+0.25-(b*x)),2)/std)
        like=pow(e,-chi/2)
        d1.append(like)
    d.append(np.mean(d1))
    b=b+0.001

p=np.array(B)
q=np.array(d)
X_Y_Spline= make_interp_spline(p,q)
X_ =np.linspace(p.min(),p.max(),500)
Y_ =X_Y_Spline(X_)

plt.plot(X_,Y_)
plt.title('keeping intercept constant')
plt.xlabel('\u03B2 (slope)')
plt.ylabel('Likelihood function')
plt.show()

"Calculating the area of likelihood vs intercept plot and finding 1 sigma errors" 
area=0
t=0
for (x,y) in zip(A,c):
    s=c[t]+c[t+1]
    area=area+(0.5*s*0.01)
    t=t+1
    if ((0.34*(1*0.43))-0.005) < area < ((0.34*(1*0.43))+0.005):
        print('34%= ', A[t])
    if ((0.68*(1*0.43))-0.005) < area < ((0.68*(1*0.43))+0.005):
        print('68%= ', A[t])
    if t==199:
        break

print('Area for Likelihood Vs Intercept plot= ', area)

"Calculating the area of likelihood vs slope plot and finding 1 sigma errors" 
area=0
t=0
for (x,y) in zip(B,d):
    s=d[t]+d[t+1]
    area=area+(0.5*s*0.01)
    t=t+1
    if ((0.34*(1*0.3812))-0.005) < area < ((0.34*(1*0.3812))+0.005):
        print('34%= ', A[t])
    if ((0.68*(1*0.3812))-0.005) < area < ((0.68*(1*0.3812))+0.005):
        print('68%= ', A[t])
    if t==199:
        break

print('Area for Likelihood Vs slope plot= ', area)