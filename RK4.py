# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 08:37:57 2021

@author: Ezra
"""

import numpy as np
import matplotlib.pyplot as plt

def f1(t,u1,u2):
    return 3*u1+2*u2-(2*t**2+1)*np.exp(2*t)

def f2(t,u1,u2):
    return 4*u1+u2+(t**2 + 2*t - 4)*np.exp(2*t)


def rk4(a,b,n,u10,u20):
    h=(b-a)/n
    u1Vec=[u10]
    u2Vec=[u20]
    tVec=[a]
    t=a
    for i in range(n):
        k1u1=h*f1(t,u10,u20)
        k1u2=h*f2(t,u10,u20)
        k2u1=h*f1(t+h/2,u10+k1u1/2,u20+k1u2/2)
        k2u2=h*f2(t+h/2,u10+k1u1/2,u20+k1u2/2)
        k3u1=h*f1(t+h/2,u10+k2u1/2,u20+k2u2/2)
        k3u2=h*f2(t+h/2,u10+k2u1/2,u20+k2u2/2)
        k4=h*f1(t+h,u10+k3u1,u20+k3u2)
        k4=h*f2(t+h,u10+k3u1,u20+k3u2)
        u10=u1-+
        t=t+h
        wVec.append(w)
        tVec.append(t)