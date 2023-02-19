from cmath import e, sin
from ctypes.wintypes import FLOAT
import math
import re 
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.interpolate import make_interp_spline
from scipy.spatial import ConvexHull

x0p=0;y0=1;z0=0;h1=0.0001
n=float(input('For which polytrope do you want the solution? \n'))
t=float(input('For what value do you require the solution? \n'))


def f(x0,y0,z0,n):
    z=-x0*x0*pow(y0,n);
    return z

def g(x0,y0,z0):
    return z0/pow(x0,2)

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

print(y0)