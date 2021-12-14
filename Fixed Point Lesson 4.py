# -*- coding: utf-8 -*-

import math

def FPIter(numIter,p0,tol):

    """
    Created on Fri Aug 27 08:22:22 2021
    FPIter(numIter,p0,tol)  is a function to find fixed points of a given
        function definded by f(x) below
    
    Input- numIter is the max number of iterations
        p0 is the intial guess of teh fixed point
        tol is the desired tolerance between successive estimates
        
    Output- p is the fixed point
        i is the number of iterations it required to get there
        
    @author: Ezra
    """
    i=1
    while i <= numIter:
        p = g(p0)
        if abs(p-p0) < tol:
            return p, i
        i = i+1
        p0=p
    
def g(x):
    #return (3*x-math.exp(x)+x**2)/x
    return(x**2+x-3)

root,iterations = FPIter(100,1.5,0.00001)
print(root,iterations)