# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:09:43 2021

@author: Ezra
"""

import numpy as np
import matplotlib.pyplot as plt

G = 10
M = 200

def f(r):
    x,y,vx,vy = r
    s = np.hypot(x,y)
    dvxdt = -G*M*x/s**3
    dvydt = -G*M*y/s**3 
    return np.array([vx,vy,dvxdt,dvydt],float)

a = -10.0
b = 10.0
N = 1000.0
h = (b-a)/N

t = np.arange(a,b,h)

y0 = np.array([10,0,10,10],float)

def RK4(f,r,h):
    k1 = h*f(r)
    k2 = h*f(r+.5*k1)
    k3 = h*f(r+.5*k2)
    k4 = h*f(r+k3)
    return r + (k1+2*k2+2*k3+k4)/6
    
def RK4integrate(f, y0, tspan):
    u = np.zeros([len(tspan),len(y0)])
    u[0,:]=y0
    for k in range(1, len(tspan)):
        u[k,:] = RK4(f, u[k-1], tspan[k]-tspan[k-1])
    return u
    

sol_RK4 = RK4integrate(f, y0, t)
x,y,vx,vy = sol_RK4.T

plt.figure(0)
plt.plot(x,y)
plt.title("x and y")
plt.grid(True)

plt.figure(1)
plt.plot(t,y)
plt.title("y as a function of time")
plt.grid(True)

plt.figure(2)
plt.plot(t,x)
plt.title("x as a function of time")
plt.grid(True)

plt.figure(3)
plt.plot(t,vy)
plt.title("velocity in the y direction as a function of time")
plt.grid(True)

plt.figure(4)
plt.plot(t,vx)
plt.title("velocity in the x direction as a function of time")
plt.grid(True)

plt.figure(5)
plt.plot(x,vx)
plt.title("velocity in the x direction as a function of x")
plt.grid(True)

plt.figure(6)
plt.plot(y,vy)
plt.title("velocity in the y direction as a function of y")
plt.grid(True)
