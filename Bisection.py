# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 07:59:39 2021

@author: Ezra

Bisection Method Impolementation to find a root of p of a function 
g(x), i.e. g(p)=0. Estimates for the left and right must ensure that f(left)*f(right)<0. 

bisection(left, right, tol, numIter)

Inputs:
    left-left side approximation bounding the root
    right-right side approximation bounding the root
    tol-tolerance (close enough)
    numIter-Maximum number of iterations.
    
Output:
    approximate solution p, and f(p) or message failure
    
Dependencies:
    user must enter function to e tested in f(x)
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def bisection(left, right, tol, numIter):

    i = 1
    fa= f(left)
    err = []

    while i <= numIter:
        p= left+(right-left)/2
        fp= f(p)
        if (fp == 0 or abs(fp) <tol):
            break
        i=i+1
        if fa*fp > 0:
            left = p
            fa=fp 
        else:
            right = p

    return p,fp,err,i   
            

def f(x):
    return(3*x - math.exp(x)) 
    
p,fp,err,i = bisection(0,1,0.00001,50)    
print(p, i)
    
