# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:28:29 2021

@author: Ezra
"""


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #return x*x*np.log(x)
    return np.sin(x)
    

def trap(a,b,n):
    '''
    Trapazoidal method of integration

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    xi : TYPE
        DESCRIPTION.

    '''
    h = (b-a)/n
    xi0=f(a) + f(b)
    for i in range(1,n):
        x = a + i*h
        xi0 = xi0 + 2*f(x)
    xi = (h*xi0)/2
    return xi 

def simp(a,b,n):
    '''
    simpsons method

    Parameters
    ----------
    a : left limit of integration
    b : right limit of integration
    n : number of subdivision for composite (even).

    Returns
    -------
    None.

    '''
    h = (b-a)/float(n)
    xi0 = f(a) + f(b)
    xi1 = 0
    xi2 = 0
    for i in range(1,n):
        x=a+i*h
        if i%2==0:
            xi2=xi2+f(x)
        else: 
            xi1=xi1+f(x)
    xi=h*(xi0+2*xi2+4*xi1)/3
    return xi

def romT4(a,b,n):
    return((4*trap(a,b,n)-trap(a,b,n))/3)

def romT6(a,b,n):
    return((16*romT4(a,b,2*n)-romT4(a,b,n))/15)

def mid(a,b,n):
    h=(b-a)/(n+2)
    xi0=0
    for i in range(int(n//2)+1):
        x=a+(2*i+1)*h
        xi0=xi0+f(x)
    xi=2*h*xi0
    return xi

a=0
b=2
soln=np.cos(a)-np.cos(b)

def err(x,y):
    z = abs(x-y)/y
    return z

est1 = trap(0,2,10)
est2 = simp(0,2,10)
est3 = mid(0,2,10)
est4 = romT4(0,2,10)
est5 = romT6(0,2,10)
print(est1)
print(est2)
print(est3)
print(est4)
print(est5)

trapEst = []
midEst = []
simEst = []
rombT4Est = []
rombT6Est = []

n=[2,10,40,50,60,100,200]

for i in range(len(n)):
    trapEst.append(err(trap(a,b,n[i]),soln))
    midEst.append(err(mid(a,b,n[i]),soln))
    simEst.append(err(simp(a,b,n[i]),soln))
    rombT4Est.append(err(romT4(a,b,n[i]),soln))
    rombT6Est.append(err(romT6(a,b,n[i]),soln))
    
# print((f(1.5)+f(1))/2*.5)


plt.figure(0)
plt.semilogy(n,trapEst,label = 'Trapezoid')
plt.semilogy(n,midEst,label = 'Midpoint')
plt.semilogy(n,simEst,label = 'Simpson')
plt.semilogy(n,rombT4Est,label = 'Romber Trap 4')
plt.semilogy(n,rombT6Est,label= 'Romber Trap 6')
