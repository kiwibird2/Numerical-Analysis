# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 07:52:36 2021

@author: Ezra
"""

import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd


def f(t,y):
    return y+np.cos(t)-t*t

def fa(t,y):
    return (1/2)*(4-np.exp(t)+4*t+2*t*t-np.cos(t)+np.sin(t))

def fp(t,y):
    return f(t,y)-np.sin(t)-2*t

def fdp(t,y):
    return fp(t,y)-np.cos(t)-2

def ftp(t,y):
    return fdp(t,y)+np.sin(t)

def fqp(t,y):
    return ftp(t,y)+np.cos(t)

def euler(n,a,b,alpha):
    '''
    Parameters
    ----------
    n : integer
        number of steps.
    a : float
        starting value for iVar.
    b : tuple
        ending value for iVar.
    alpha : float
        intial condition.

    Returns
    -------
    t : float
        time.
    w : float
        dVar.
    '''
    h=(b-a)/n
    t=a
    w=alpha
    for i in range(n):
        w=w+h*f(t,w)
        t=t+h
    return t,w

def taylor2(n,a,b,alpha):
    '''
    Parameters
    ----------
    n : integer
        number of steps.
    a : float
        starting value for iVar.
    b : tuple
        ending value for iVar.
    alpha : float
        intial condition.

    Returns
    -------
    t : float
        time.
    w : float
        dVar.
    '''
    h=(b-a)/n
    t=a
    w=alpha
    for i in range(n):
        w=w+h*f(t,w) + (h*h/2) * fp(t,w)
        t = t+h
    return t,w

def taylor4(n,a,b,alpha):
    '''
     See taylor 2
    '''
    h=(b-a)/n
    t=a
    w=alpha
    for i in range(n):
        w=w+h*f(t,w) + (h*h/2) * fp(t,w)+(h**3/6)*fdp(t,w)+(h**4/24)*ftp(t,w)
        t = t+h
    return t,w

def taylor6(n,a,b,alpha):
     '''
      See taylor 2
     '''
     h=(b-a)/n
     t=a
     w=alpha
     for i in range(n):
        w=w+h*f(t,w) + (h*h/2) * fp(t,w)+(h**3/6)*fdp(t,w)+(h**4/24)*ftp(t,w)+(h**5/120)*fqp(t,w)
        t = t+h
     return t,w

def err(x,y):
    '''
    Parameters
    ----------
    x : approximate solution
    y : exact solution

    Returns
    -------
    relative error between x and y
    '''
    return abs((y-x)/y)

yEval= 2
anaSoln = fa(yEval, 34.2343)
t,eulerSoln = euler(20,0,yEval,1)

n = np.array([10,20,50,100,200,1000])
eulerErr = []
t2Err = []
t4Err=[]
t6Err=[]

y1=np.linspace(0,4,20)
t,esol=euler(20,0,y1,1)
t,t2=taylor2(20,0,y1,1)
t,t4=taylor4(20,0,y1,1)
t,t6=taylor6(20,0,y1,1)
ana=fa(y1,34.2343)

plt.figure(0)
plt.grid(True)
plt.title("Plot of approximate solution of y=f(t,y)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(y1,esol,label="euler")
plt.plot(y1,t2,label="taylor2")
plt.plot(y1,t4,label="taylor4")
plt.plot(y1,t6,label="taylor6")
plt.plot(y1,ana,label="analytic")
plt.legend()
plt.show()


for i in range(len(n)):
    t,eulerSoln = euler(n[i],0,yEval,1)
    eulerErr.append(err(eulerSoln,anaSoln))
    t,t2Soln = taylor2(n[i],0,yEval,1)
    t2Err.append(err(t2Soln,anaSoln))
    t,t4Soln = taylor4(n[i],0,yEval,1)
    t4Err.append(err(t4Soln,anaSoln))
    t,t6Soln = taylor6(n[i],0,yEval,1)
    t6Err.append(err(t6Soln,anaSoln))
    
    
error=pd.DataFrame({'eulerErr': eulerErr,'t2Err':t2Err,'t4Err':t4Err,
                        't6Err':t6Err})
file_name='techlab4error.xlsx'
error.to_excel(file_name)

print("Analytic Soln:", anaSoln, "Euler Soln:", eulerSoln, "Difference",
      anaSoln-eulerSoln, "taylor2:", t2Soln, "taylor4:", t4Soln)

plt.figure(1)
plt.grid(True)
plt.title("Plot of Relative Error at t=2")
plt.xlabel("n")
plt.ylabel("Relative Error")
plt.semilogy(n,eulerErr,label="euler")
plt.semilogy(n,t2Err,label="taylor2")
plt.semilogy(n,t4Err,label="taylor4")
plt.semilogy(n,t6Err,label="taylor6")
plt.legend()
plt.show()


print(eulerErr, "test")


'''
Solution to the Gompertz differential equation using eulers method
'''

z=.0439
K=12000.0
def G(t,N):
    return z*np.log(K/N)*N

# def Gp(t,N):
#     return z*K+z*np.log(K/N)*G(t,N)


def euler2(n,a,b,alpha):
    h=(b-a)/n
    t=a
    w=alpha
    for i in range(n):
        w=w+h*G(t,w)
        t=t+h
    return t, w

# def taylor22(n,a,b,alpha):
#     h=(b-a)/n
#     t=a
#     w=alpha
#     for i in range(n):
#         w=w+h*G(t,w) + (h*h/2) * Gp(t,w)
#         t = t+h
#     return t,w


x1=np.linspace(0, 100, 1000, endpoint=True)
t, eulerSoln = euler2(20,0,x1,4000)
# t,t23=taylor22(20,0,x1,4000)

#print(t, eulerSoln, "test")

plt.figure(2)
plt.grid(True)
plt.title("Gompertz solution plot")
plt.xlabel("t")
plt.ylabel("cells")
plt.plot(t,eulerSoln,label="euler")
# plt.plot(t,t23,label="taylor2")
plt.legend
plt.show()


def Iter(numIter,p0,tol):
    '''
    

    Parameters
    ----------
    numIter : integer
        how many cells in the tuple you want it to check.
    p0 : float
        value you are looking for.
    tol : float
        how close you need the value to be for it to return the cell.

    Returns
    -------
    p : float
        the value that it found within the tol.
    i : float
        the value of the cell.
    '''
    i=1
    while i <= numIter:
        p=eulerSoln[i]
        if abs(p-p0) < tol:
            return p,i
        i = i+1

p,m=Iter(1000,11000,10)

print(p,m)
