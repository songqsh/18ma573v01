#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:41:38 2018

@author: songqsh

Finite Difference Method for 1_d heat equation
Explicit scheme
"""

import numpy as np


'''
heat equation setup
'''

al = 1. #diffusivity


a = 0; b = 1. #boundary of space domain


f = lambda x: np.sin(np.pi * x) #Initial data

g = lambda t: 0 #boundary data at a
h = lambda t: 0 # boundary data at b


#exact solution, if available
u_exact = lambda x,t: np.exp(-np.pi**2*t) * np.sin(np.pi*x)

#terminal time
T = 2

'''
ftcs computation
input: 
    dx: space mesh size
    rho: conditional number
return:
    u: ndarray shape = (N+1)*(M+1)
    x_mesh: ndarray shape = (N+1)
    t_mesh: ndarray shape = (M+1)
'''

def ftcs_heat_1d(dx, rho):
    
    dt = rho*(dx**2)/al #time step size
    '''
    fdm paras computing
    '''
    
    N = int((b-a)/dx)
    M = int(T/dt)
    x_mesh = dx*np.arange(N+1)
    t_mesh = dt*np.arange(M+1)
    
    u = np.zeros((N+1, M+1)) #initialize value function
    
    u[:,0] = f(x_mesh) #initial data
    u[0,:] = g(t_mesh) #lower boundary data
    u[N,:] = h(t_mesh) #upper boundary data
    
    
    '''
    interior update
    '''
    for k in np.arange(1,M+1):
        for i in np.arange(1, N):
            u[i, k] = rho * u[i-1, k-1] + (1-2*rho)*u[i,k-1] + rho*u[i+1,k-1]
            
    return u, x_mesh, t_mesh


if __name__ == "__main__":       

    '''
    ftcs computation
    '''
        
    dx = .2 #space mesh size
    rho = .2 #conditinal number, to be less than .5 for the stability
    dt = rho*(dx**2)/al #time step size

    u, x_mesh, t_mesh = ftcs_heat_1d(dx, rho)


    '''
    error 
    '''
    TT, XX = np.meshgrid(t_mesh, x_mesh)    
    error = u - u_exact(XX,TT)
    
    print('rho is:' + str(rho))
    print('max error:' + str(np.max(np.abs(error))))
    
    
    
    import matplotlib.pyplot as plt
    M = t_mesh.size -1
    fig1 = plt.figure()
    for i in np.arange(M-2, M+1):
        plt.plot(x_mesh, error[:,i], label = 't = '+ str(round(i*dt,2)))
    plt.legend()    
    
    
    

        
    '''
    plot surface
    '''
       
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm

    fig = plt.figure()
    ax = fig.gca(projection='3d')


    surf_num = ax.plot_surface(XX,TT, u, cmap=cm.coolwarm)
    






