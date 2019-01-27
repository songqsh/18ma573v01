
# coding: utf-8

# # Euler scheme on 2-d SDE
# 
# ## General 2-d SDE

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


'''=========
sde_2d class init
=========='''

class Sde_2d:
    def __init__(self,
                init_state = [100., .04],
                drift = lambda x: [0.01, 0.03], #x: 2-d array
                vol = lambda x: [[0.1, 0], [0,0.1]], #x: 2-d array, vol: 2 by 2 array
                ):
        self.init_state = init_state
        self.drift = drift
        self.vol = vol
        


# In[3]:


'''================
euler_2d_difference 
input:
    xh_i: 2_d current state
    dt: 1_d time diff
    dw: 2_d bm increase
output:
    xh_i_diff: 2_d increase for euler solution
=================='''

def euler_2d_diff(self, xh_i, dt, dw):
    #set SDE param
    mu = self.drift
    sigma = self.vol
    
    return np.array(mu(xh_i))*dt + np.matmul(sigma(xh_i), dw)

Sde_2d.euler_diff = euler_2d_diff


# In[4]:


'''==========
euler method as a method of SDE_2d
input:
    time grid: np.array (t_i: i = 0, 1, ..., n)
output: 
    euler solution: np.array (Xh_i: i = 0, 1, ..., n)
==========='''

def euler_2d(self, grid):
    #step_size dt
    dt = np.diff(grid)
    
    #generate 2d bm icrement
    dw = np.array([np.random.normal(0, np.sqrt(dt)) for i in range(2)])

    #initialize euler solution
    x0 = self.init_state #2_d array
    xh = np.array([x0[i] + np.zeros(grid.shape) for i in range(2)])
 
    
    #run euler
    for i in range(dt.size):
        xh[:,i+1] = xh[:,i] + self.euler_diff(xh[:,i], dt[i], dw[:,i]) #euler iteration        
    return xh

Sde_2d.euler = euler_2d


# In[5]:



# ## Heston model

# In[6]:


'''============
Heston class inherited from sde_2d
============='''

class Heston(Sde_2d):
    def __init__(self,
                 init_state = [100., .04],
                 r = .05,
                 kappa = 1.2,
                 theta = .04,
                 xi = .3,
                 rho = .5,
                ):
        self.init_state = init_state
        rho_bar = np.sqrt(1 - rho**2)
        self.drift = lambda x: [r*x[0], kappa*(theta -x[1])]
        self.vol = lambda x: [
            [np.sqrt(x[1])*x[0], 0], 
            [xi*np.sqrt(x[1])*rho, xi*np.sqrt(x[1])*rho_bar]
        ]
                              


# In[7]:


'''================
euler_2d_difference for Heston class to overide SDE_2d class member

input:
    xh_i: 2_d current state
    dt: 1_d time diff
    dw: 2_d bm increase
output:
    xh_i_diff: 2_d increase for euler solution
=================='''

def euler_heston_diff(self, xh_i, dt, dw):
    #set SDE param
    mu = self.drift
    sigma = self.vol
    xh_i[1] = np.max([0, xh_i[1]]) #new line to override
    
    return np.array(mu(xh_i))*dt + np.matmul(sigma(xh_i), dw)

Heston.euler_diff = euler_heston_diff #override


# In[8]:




if __name__ == '__main__':    
    
        
    '''=============
    test SDE_2d.euler
    plot paths
    =============='''
    sde1 = Sde_2d(init_state=[100., .04], 
                  drift=lambda x:[.01, .03], 
                  vol= lambda x:[[.1, 0],[0, .1]]
                  )
    grid = np.linspace(0,1,100)
    num_path = 5
    path = [sde1.euler(grid) for i in range(num_path)] #path container
    
    
    plt.figure()
    
    
    plt.subplot(2,1,1)
    plt.title('Sde_2d.euler')
    plt.ylabel('1st state')
    for i in range(num_path):
        plt.plot(grid, path[i][0]) #first dimension of the path

    plt.subplot(2,1,2)
    plt.ylabel('2nd state')
    for i in range(num_path):
        plt.plot(grid, path[i][1]) #first dimension of the path



    
    '''==========
    test plot euler paths for Heston
    =========='''
    heston1 = Heston(init_state=[100., .04], r=.05, 
                     kappa=1.2, theta=.04, xi=.3, rho=.5)
    
    grid = np.linspace(0,1,100)
    num_path = 5
    path = [heston1.euler(grid) for i in range(num_path)] #path container
    
    
    plt.figure()
    
    
    plt.subplot(2,1,1)
    plt.title('Henston.euler')
    plt.ylabel('1st state')
    for i in range(num_path):
        plt.plot(grid, path[i][0]) #first dimension of the path

    plt.subplot(2,1,2)
    plt.ylabel('2nd state')
    for i in range(num_path):
        plt.plot(grid, path[i][1]) #first dimension of the path