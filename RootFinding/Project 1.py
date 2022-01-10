# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:01:38 2021

@author: Ezra
"""

import math
import matplotlib.pyplot as plt


def f(x):
    return math.cos(x)

  
def Secant(p0,p1,tol,maxIter):
    """
    

    Parameters
    ----------
    p0 : float
        Value to intialize secant method.
    p1 : float
        Second value to intialize secant method.
    tol : float
        The tolerance of the program when determining the root
        of the function vs the root of the secant line.
    maxIter : integer
        Maximum number of iterations the program will run before
        it gives up.

    Returns
    -------
    p : float
        This is the calculated value of the root of the function.
    i : integer
        the amount of times it took to get there.

    """
    
    i = 2
    q0=f(p0)
    q1=f(p1)
    
    while i < maxIter:
        p = p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<tol:
            return p,i
        i=i+1
        p0=p1
        q0=q1
        p1=p
        q1=f(p)
       
k,i =Secant(0,math.pi,.00001,100)

print("the root for cos(x) between 0 and Pi:", k, "and the iterations it took to get there:", i)

def g(x):
    return 1-math.cos(x)

def Secant(p0,p1,tol,maxIter):
    
    i = 2
    q0=g(p0)
    q1=g(p1)
    
    while i < maxIter:
        p = p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<tol:
            return p,i
        i=i+1
        p0=p1
        q0=q1
        p1=p
        q1=g(p)
       
k,i =Secant(0,math.pi,.00001,100)

print("the root for 1-cos(x) between 0 and Pi:", k, "and the iterations it took to get there:", i)

P=70000
x=32
d= 2400

def h(j):
    return -200000+((P*(1+(j))**x))+(d/(j))*(((1+(j))**x)-1)

r=[]
s=[]
n=0.001
N0=.025
while n < N0:
    o=h(n)
    r.append(100*(12*n))
    s.append(o)
    n=n+.001

def Secant(p0,p1,tol,maxIter):
    
    i = 2
    q0=h(p0)
    q1=h(p1)    
    
    while i < maxIter:
        p = p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<tol:
            return p,i
        i=i+1
        p0=p1
        q0=q1
        p1=p
        q1=h(p) 
       
k,i =Secant(.01,.2,.00001,100)

print("the interest rate required for COL Lindquist to purchase his RV:", k, "and the iterations it took to get there:", i)

def w(x):
    return x**2-10

def Secant(p0,p1,tol,maxIter):
    
    i = 2
    q0=g(p0)
    q1=g(p1)
    
    while i < maxIter:
        p = p1-q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<tol:
            return p,i
        i=i+1
        p0=p1
        q0=q1
        p1=p
        q1=w(p)
       
k,i =Secant(5,10,.00001,100)

#print("the root for x^2-1 between 0 and 10:", k, "and the iterations it took to get there:", i)

plt.plot(r,s)
plt.grid()
