# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:41:19 2021

@author: Ezra
"""

import numpy as np
import time
import pandas as pd

def f(x):
    return -x*np.sin(x)-x*x/4*np.cos(x)

def fPrime(x):
    return x**2/4*np.sin(x)-3*x/2*np.cos(x)-np.sin(x)


def fwdDiff(x0,h):
    dfdx=(f(x0+h)-f(x0))/h
    return dfdx


def bacDiff(x0,h):
    dfdx=(f(x0)-f(x0-h))/h
    return dfdx

def cenDiff(x0,h):
    dfdx=(f(x0+h)-f(x0-h))/(2*h)
    return dfdx

def fourthOrdDiff(x0,h):
    dfdx = (4*cenDiff(x0, h/2)-cenDiff(x0,h))/3
    return dfdx


def sixthOrdDiff(x0,h):
    dfdx=(16*(fourthOrdDiff(x0, h/2))-fourthOrdDiff(x0, h))/15
    return dfdx


x0=np.array([-3,-2.5,-2,-1.5,-1,-.5,0,.5,1,1.5,2,2.5,3])

t1 = time.perf_counter()
fde=fwdDiff(x0,.1)
tfwd  = time.perf_counter()-t1
print("time to run fwdDiff", tfwd)

t2 = time.perf_counter()
bde=bacDiff(x0,.1)
tbc  = time.perf_counter()-t2
print("time to run bacDiff", tbc)

t3 = time.perf_counter()
cde=cenDiff(x0,.1)
tcen  = time.perf_counter()-t3
print("time to run cendiff", tcen)

t4 = time.perf_counter()
foe=fourthOrdDiff(x0, 0.1)
tfourth  = time.perf_counter()-t4
print("time to run fourthOrdDiff", tfourth)

t5 = time.perf_counter()
soe=sixthOrdDiff(x0,.1)
tsix  = time.perf_counter()-t5
print("time to run sixthOrdDiff", tsix)

act=fPrime(x0)

print("Forward Difference Estimate=", fde)
print("Backwards Difference Estimate=", bde)
print("Center Difference Estimate=", cde)
print("Fourth Order Difference Estimate=", foe)
print("Sixth Order Difference Estimate=", soe)
print("Analytic Value of Derivative=", act)

def err(x,y):

    return abs((y-x)/y)

h=np.array([.5,.5**2,.5**3,.5**4,.5**5])

x0=1
analytical= fPrime(x0)
errFwd=[]
errCen=[]
errBac=[]
errFourthOrder=[]
errSixthOrder=[]
dfdxFwd=[]
dfdxBac=[]
dfdxCen=[]
dfdxFourth=[]
dfdxSixth=[]

for i in range(len(h)):
    dfdxFwd.append(fwdDiff(x0,h[i]))
    dfdxBac.append(bacDiff(x0,h[i]))
    dfdxCen.append(cenDiff(x0,h[i]))
    dfdxFourth.append(fourthOrdDiff(x0,h[i]))
    dfdxSixth.append(sixthOrdDiff(x0, h[i]))
    errFwd.append(err(dfdxFwd[i],analytical))
    errBac.append(err(dfdxBac[i],analytical))
    errCen.append(err(dfdxCen[i],analytical))
    errFourthOrder.append(err(dfdxFourth[i],analytical))
    errSixthOrder.append(err(dfdxSixth[i],analytical))

    
import matplotlib.pyplot as plt
    
plt. figure(0)
plt.semilogy(h,errFwd,label="FWD")
plt.semilogy(h,errBac,label="BAC")
plt.semilogy(h,errCen,label="CEN") 
plt.semilogy(h,errFourthOrder,label="FTH")
plt.semilogy(h,errSixthOrder,label="SIX")
plt.title("Error of methods of various orders")
plt.xlabel("h")
plt.ylabel("Relative error")
plt.grid(True)
plt.legend()
plt.show()


x=np.linspace(-5,5,100)
z=np.linspace(-5,5,20)

plt.figure(1)
plt.plot(x,fPrime(x),label="Analytic")
plt.scatter(z,fwdDiff(z, .1),color='red',label= 'fwdDiff')
plt.scatter(z,bacDiff(z, .1),color='green',label='bacDiff')
#plt.scatter(z,cenDiff(z, .1),color='orange',label="cenDiff")
plt.scatter(z,fourthOrdDiff(z, .1),color='pink',label="4thOrdDiff")
plt.title("graph of function using cenDiff and analytic solution")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()



dfdxFwd=tuple(dfdxFwd)
dfdxBac=tuple(dfdxBac)
dfdxCen=tuple(dfdxCen)
dfdxFourth=tuple(dfdxFourth)
dfdxSixth=tuple(dfdxSixth)
errFwd=tuple(errFwd)
errBac=tuple(errBac)
errCen=tuple(errCen)
errFourthOrder=tuple(errFourthOrder)
errSixthOrder=tuple(errSixthOrder)

Estimates=pd.DataFrame({'FwdDiff': dfdxFwd,'BacDiff':dfdxBac,'CenDiff':dfdxCen,
                        'FourthOrdDiff':dfdxFourth,'SixthOrdDiff':dfdxSixth,
                        'errFwd':errFwd,'errBac':errBac,'errCen':errCen,
                        'errFourthOrder':errFourthOrder,'errSixthOrder':errSixthOrder})
file_name='dfdx.xlsx'
Estimates.to_excel(file_name)