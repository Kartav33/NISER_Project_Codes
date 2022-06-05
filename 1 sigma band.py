from cmath import e
import math 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pan
import random
from scipy.interpolate import make_interp_spline
from scipy.spatial import ConvexHull
import mpl_toolkits.mplot3d 
import statistics

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
#plt.show()

"Generating a list of a million points for the intercept"
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

aleft= np.random.normal(loc=-0.25,scale=0.07,size=1470000)
aright=np.random.normal(loc=-0.25,scale=0.08,size=1470000)
Aleft=[];Aright=[]
for item in aright:
    if -0.25 <= item <= -0.17:
        if len(Aright) == 500000:
            break
        Aright.append(item)

for item in aleft:
    if -0.32 <= item < -0.25:
        if len(Aleft) == 500000:
            break
        Aleft.append(item)

Afinal=Aleft+Aright


"Generating a list of a million points for the slope"
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

bleft= np.random.normal(loc=0.22,scale=0.08,size=1470000)
bright=np.random.normal(loc=0.22,scale=0.06,size=1470000)
Bleft=[];Bright=[]
for item in bright:
    if 0.22 <= item <= 0.28:
        if len(Bright) == 500000:
            break
        Bright.append(item)

for item in bleft:
    if 0.14 <= item < 0.22:
        if len(Bleft) == 500000:
            break
        Bleft.append(item)

Bfinal=Bleft+Bright

"For each ordered million pairs, we are generating an estimated time. Here, we get million such point, from which we plotted the mean and 1 sigma deviation "
t=10
for item in range(1,101):
    Yfinal=[]
    for (x,y) in zip(Afinal,Bfinal):
        y=(t*y)+x
        Yfinal.append(y)
    ym=np.mean(Yfinal)
    ystd=statistics.stdev(Yfinal)
    plt.scatter(t,ym,color='blue')
    plt.scatter(t,ym-ystd,color='green')
    plt.scatter(t,ym+ystd,color='green')
    t=t+0.03

plt.show()