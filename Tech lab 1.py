# -*- coding: utf-8 -*-
def fibSumThree(n0):
    
    """
Created on Mon Aug 23 07:40:53 2021

@author: Ezra

fibSumThree(n0) function to find the sum of all the terms in the
Fibonacci sequence divisible by three whih do not exceed n0.

Input: n0 is the largest natural number considered

Output: fibSumThree- the sum of the Fibonacci terms divisible by 3 that do
not exceed n0.
  
    """
    
    a=0
    b=1
    fibSum3 = 0
    while b < n0:
        if b % 3 == 0 :
            fibSum3 = fibSum3 + b
            
        c =a+b
        a=b
        b=c
    print("b=", "fibSum3",fibSum3)        
    return fibSum3
    
fibSumThree(500000000)

def fibSumThreeTracker(n0):
    
    """
Created on Mon Aug 23 07:40:53 2021

@author: Ezra

fibSumThree(n0) function to find the sum of all the terms in the
Fibonacci sequence divisible by three whih do not exceed n0.

Input: n0 is the largest natural number considered

Output: fibSumThreeTracker- 
    x: Fibonacci numbers taht are divisible by 3
    y: The sum of the Fibonacci terms divisible by 3
    that do not exceed n0
    
the sum of the Fibonacci terms divisible by 3 that do
not exceed n0. keeps track of intermeiate values.
  
    """
    
    a=0
    b=1
    fibSum3 = 0
    x=[]
    y=[]
    
    while b < n0:
        if b % 3 == 0 :
            fibSum3 = fibSum3 + b
            x.append(b)
            y.append(fibSum3)
            
        c =a+b
        a=b
        b=c
    return x,y
    print("b=", "fibSum3",fibSum3)        
    return fibSum3

x,y = fibSumThreeTracker(500000000)
print(x)
print(y)

import matplotlib.pyplot as plt

plt.figure(0)
plt.plot(x,y)
plt.title(" A neat plot that doesn't really convey anything")
plt.xlabel("Fibonacci number")
plt.ylabel("fibSumThree")
plt.grid()
plt.show()


plt.figure(1)
plt.plot(x,y)
plt.title(" A neat plot that doesn't really convey anything")
plt.xlabel("Fibonacci number")
plt.ylabel("fibSumThree")
plt.grid()
plt.yscale('log')
plt.show()



