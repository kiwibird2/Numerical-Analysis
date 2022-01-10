# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 07:57:18 2021

@author: Ezra
"""

def brute(n,c,x0):
    """
    
    Parameters
    ----------
    n : integer
        This is the degree of the polynomial that we are seeking
        to evaluate.
    c : float
        This is the coefficients of the polynomial.
    x0 : float
        This is the point which we are evaluating the polynomial.

    Returns
    -------
    p : float
        This is the value of the function evaluated at x0.

    """
    
    
    p=0
    for i in range(n+1):
        p = p + c[i]*x0**i
    return p


n0=.5
import random
random.seed(48)
#coef=[random.randint(-50,50) for i in range(1001)]
#print(coef)

coef=[1,-3,4,-1,-16]
n = len(coef)-1
    
bruteY=brute(n,coef,0.5)
print(bruteY)

import time
t1 = time.perf_counter()
bruteY = brute(n,coef,0.5)
tBrute  = time.perf_counter()-t1
print(tBrute)

def horner(n,c,x0):
    """
    

    Parameters
    ----------
    n : integer
        degree of the polynomial.
    c : float
        coefficients of the polynomial.
    x0 : float
        where we are evaluating the polynomial.

    Returns
    -------
    y : float
        the value of the function evaluated at x0.
    z : float
        the value of the derivative evaluated at x0.

    """
    
    y=c[n]
    z=c[n]
    for i in range(n-1,0,-1):
        y= x0*y+c[i]
        z=x0*z+y
    y=x0*y+c[0] #this computes the b0
    return y,z


t0 = time.perf_counter()
hornerY, hornerZ=horner(n,coef,0.5)
tHorner = time.perf_counter()-t0

print("Value of the gigantic polynomial", hornerY, "The direvative of the gigantic polynomial:", hornerZ)
print("the time it took to compute the grigantic polynomial using Horner's method:", tHorner)