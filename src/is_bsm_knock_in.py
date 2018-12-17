#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:00:26 2018

@author: songqsh
"""

import numpy as np
from exact_simulation_v01 import bm_1d

r = .05; sigma = 0.15; s0 = 95
T = 0.25; H = 85; K = 96
#k = 1000; n = 1000; m = 50
k = 100; n = 1000; m = 50; dt = T/m

b = - np.log(H/s0); c = np.log(K/s0)
slope = (c+2*b)/T
r1 = .5*sigma**2 - slope
r2 = .5*sigma**2 + slope
th1 = (r1 - r)/sigma
th2 = (r2 -r)/sigma

val = np.zeros(k)
for ii in range(k):
    L = np.zeros(m)
    adj_payoff = np.zeros(n)
    
    for i in range(n):
        w_hat = bm_1d(T,m)
        flag = 0
        tau = T + 1
        w_hat_tau = 0
        
        #generate a path for L
        for j in range(m):
            if flag == 0:
                L[j] = sigma*w_hat[j] - slope*(j+1)*dt
                if L[j] < - b:
                    tau = (j+1)*dt
                    w_hat_tau = w_hat[j]
                    flag = 1
            else:
                L[j] = sigma*w_hat[j] -slope*tau + slope*((j+1)*dt - tau)
                
        i_payoff = 1000*float(L[-1]>c)*float(tau<T)
        likelyhood_ratio = 1./np.exp(th1*w_hat_tau + \
            th2*(w_hat[-1] - w_hat_tau) + \
            .5*th1**2*tau + .5*th2**2*(T-tau))
        adj_payoff[i] =np.exp(-r*T)*i_payoff*likelyhood_ratio
        
    val[ii] = adj_payoff.mean()


print('MC computation value: \n')
print('Mean is ' + str(val.mean()))    
print('MSE is ' + str(val.var()))