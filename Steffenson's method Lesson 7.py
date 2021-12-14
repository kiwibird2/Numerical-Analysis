# -*- coding: utf-8 -*-

def f(x):
    return 3**(-x)

def steff(p0, tol, maxIter):
    
    """
    Created on Thu Sep  2 08:44:48 2021
    
    
    
    @author: Ezra
    """
    
    i=1
    while i <maxIter:
        p1 = f(p0)
        p2 = f(p1)
        p = p0 - (p1-p0)**2/(p2-2*p1+p0)
        if abs(p-p0) <= tol:
            return (p,i)
        i=i+1
        p0 = p

def FPIter(numIter,p0,tol):
    
    i=1
    while i <= numIter: 
        p=f(p0)
        if abs(p-p0) <tol:
            return p, i
        i = i + 1
        p0 = p

root, iterations=FPIter(100,10,0.00001)
print(root,iterations)

p,i = steff(10,0.00001,100)
print(p,i)            

