# -*- coding: utf-8 -*-

import math

def f(x):
    return 3*x-math.exp(x)

def g(x):
    return 3-math.exp(x)

def newton(p0,tol,maxIter):
        
    """
    Created on Tue Aug 31 07:37:29 2021
    The function newton(p0,tol,maxIter) is designed to find the root
    of a function using newtons method. 
    
    Inputs: p0 is our intial guess for te root
            tol is the desired tolerance between successive approx.
            maxIter is the max number of iterations to try
    
    Outputs: p - the best guess for the root
             iter - how many iteration s it took to get there
    
    @author: Ezra
    """

    iter=1
    while iter < maxIter:
        p = p0 - f(p0)/g(p0)
        if abs(p-p0) < tol:
            return p, iter
        iter = iter+1
        p0=p
        
p,iter = newton(0.5,.000001,100)
print("Root is:",p,"Number of iterations =", iter)