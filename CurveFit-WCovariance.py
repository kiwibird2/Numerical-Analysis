# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 08:31:20 2022

@author: Ezra
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(t,A,w,phi):
    y = A*np.sin(w*t+phi)
    return y

data1 = pd.read_csv(r'fileDirectory')

x = data1['time (s)']
y = data1['displacement (m)']
t = np.linspace(0,10)


init_guess = [1.5,1.5,0]

ans,cov = curve_fit(f, x, y, p0=init_guess)
fit_A, fit_w, fit_phi = ans

plt.figure(1)
plt.plot(t,f(t,fit_A,fit_w,fit_phi), 'r')
plt.plot(x,y,'.',color='black')
plt.legend(['fit', 'data'])
plt.figtext(.92,.85, 'A = -.249 +/- 2E-6 m' )
plt.figtext(.92,.75, 'w = 1.87 +/- 4E-6 rad/s')
plt.figtext(.92,.65, 'phi = -2.51 +/- .0001 rad')
plt.figtext(.92,.55, 'y = -.249*sin(1.87*t-2.51)')
plt.xlabel('t [s]')
plt.ylabel('y(t), [m]')
plt.title('fit of a harmonic oscillator')
plt.grid()
plt.show()