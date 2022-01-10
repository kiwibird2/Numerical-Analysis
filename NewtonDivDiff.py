# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:10:02 2021

@author: joseph.lindquist
"""

import numpy as np
import matplotlib.pyplot as plt

def divDiff(x0,y0):
    """
    Compute the Newton divided difference coefficients for an interpolant: 
    
    Input: 
        x0 - vector of "x"
        y0 - vector of "y"
    Output:
        nCoef - vector of newton coefficients
    """
    n = len(x) # Number of data points
    coef = np.zeros((n,n)) # create a matrix that is n x n
    nCoef = np.zeros(n)
    nCoef[0]=y0[0] # seed a_0
    for i in range(n): # fill in f[x_n] using y0 values
        coef[i,0]=y0[i] 
    for i in range(1,n): # cycle through 1,2,...,n including the nth
        for j in range(1,i+1):
            coef[i,j]=(coef[i,j-1]-coef[i-1,j-1])/(x0[i]-x0[i-j])
        nCoef[i]=coef[i,i] # record coefficient on diagonal for a_i
    print(coef)
    return nCoef

def newtonEval(coef,x0,xE):
    """
    Evaluate the polynomial given by the Newton coefficients of the form: 
        P_n(x)=a0 + a1(x-x0) + a2(x-x0)(x-x1) + ... + a_n(x-x0)...(x-x_n-1)
    Input:
        coef - array returned by the divDiff function
        x0   - vector of data points
        xE   - node to interpolate at
    Output: 
        val  - value of interpolant at x=xE, i.e. P(xE)
    Dependencies:
        Requires use of divDiff
    """
    #We need to figure this out in class!
    n = len(coef)-1
    val = coef[n]
    i = n-1
    while i >= 0:
        val = val * (xE-x[i])+coef[i]
        i = i - 1
    return val

def unitStep(n):
    """
    Creates n interpolation points for a unit step function, centered at 0. 
    Uses uniformly spaced interpolation points. 
        
    Input: 
        n - number of interpolation points desired
    
    Output:
        x - vector of "x"
        y - vector of "y"
    """
    x = np.linspace(-1,1,n) # create some interpolation points
    y = np.ones(len(x)) # "y" values for the given interpolation points above
    for i in range(len(x)):
        if x[i] <= 0:
            y[i]=0
    return x,y

def unitStepCheb(n):
    """
    Creates n interpolation points for a unit step function, centered at 0
    Uses the roots of Chebychev polynomials for interpolation points. 
        
    Input: 
        n - number of interpolation points desired
    
    Output:
        x - vector of "x"
        y - vector of "y"
    """    
    x = np.zeros(n)
    y = np.ones(n)
    for i in range(n):
        x[i] = np.cos(((2*i+1)*np.pi)/(2*n))
        if x[i] <= 0:
            y[i]=0
    return x,y
# Some Examples

#x=np.array([1,1.3,1.6,1.9,2.2]) # Example 3.3.1
#y=np.array([0.7651977,0.620086,0.4554022,0.2818186,0.1103623])

#x = np.linspace(-1,3,10) # x values for the interpolation nodes
#y = np.cos(x) # "y" values for the cosine interpolation nodes

#x,y = unitStep(20)

x,y = unitStepCheb(20)

# Find the Newton Divided Difference Coefficients
coef=divDiff(x,y)
print(coef)

# Interpolate at a point. 
print(newtonEval(coef,x,0))

left = -1
right = 1
nPoints = 100
xInterp = np.linspace(left,right,nPoints)
est = np.zeros(nPoints)
for i in range(nPoints):
    est[i]=newtonEval(coef,x,xInterp[i])


# Plotting routine with legend
plt.plot(x,y,"o",color="k", label='Interp Points')
plt.plot(xInterp,est, label = 'Interpolant')
plt.ylim([-3,3])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the function')
plt.grid(True)
plt.legend()
plt.show

