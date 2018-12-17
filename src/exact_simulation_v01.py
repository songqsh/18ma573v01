#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:31:08 2018

@author: songqsh

exact simulations
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# return: ndarray size (m, )
# Let W = bm_1d(T, m)
# W[i] is value at time (i+1)*dt
def bm_1d(T, m):
    dt = T/m
    dW = np.sqrt(dt)*norm.rvs(size = m)
    return dW.cumsum()

# arethmatic bm
def abm_1d(T, m, b=1., sigma=1., x0 = 0):
    dt = T/m
    dW = np.sqrt(dt)*norm.rvs(size = m)
    dX = b*dt + sigma*dW
    X = dX.cumsum()
    return x0 + X


#geometric bm
def gbm_1d(T, m, b = 0.05, sigma = 0.15, x0 = 1):
    L = abm_1d(T, m, b - 0.5*sigma**2, sigma, 0) #normalized log process
    return x0*np.exp(L)

    

# See testing code also from      
if __name__ == '__main__':
    
    T =1; m = 100
    
    
    #generate bm
    '''
    W = np.concatenate(([0], bm_1d(T, m)))
    plt.plot(np.linspace(0, 1, m+1), W)
    
    '''
    #generate abm
    '''
    x0 = 2.
    X = np.concatenate(([x0], abm_1d(T, m, x0 = x0)))
    plt.plot(np.linspace(0, T, m+1), X)
    '''
    
    #generate gbm
    x0 = 2.
    X = np.concatenate(([x0], gbm_1d(T, m, x0 = x0)))
    plt.plot(np.linspace(0, T, m+1), X)
    
