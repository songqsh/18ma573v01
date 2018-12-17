#
# Black-Scholes-Merton (1973) European Call & Put Valuation
# 05_com/BSM_option_valuation.py
#
# (c) Dr. Yves J. Hilpisch
# Derivatives Analytics with Python
#
import math
import numpy as np
#import matplotlib.pyplot as plt
import scipy.stats as ss



def d1f(S0, K, T, r, sigma):
    ''' Black-Scholes-Merton d1 function.
        Parameters see e.g. BSM_call_value function. '''
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma ** 2)
          * T) / (sigma * math.sqrt(T))
    return d1


#
# Valuation Functions
#

def bsm_call_value(S0, K, T, r, sigma):
    ''' Calculates Black-Scholes-Merton European call option value.

    Parameters
    ==========
    St : float
        stock/index level at time t
    K : float
        strike price
    T : float
        date of maturity/time-to-maturity if t = 0; T > t
    r : float
        constant, risk-less short rate
    sigma : float
        volatility

    Returns
    =======
    call_value : float
        European call present value at t
    '''
    d1 = d1f(S0, K, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T)
    call_value = S0 * ss.norm.cdf(d1) - math.exp(-r * T) * K * ss.norm.cdf(d2)
    return call_value


def bsm_put_value(S0, K, T, r, sigma):
    ''' Calculates Black-Scholes-Merton European put option value.

    Parameters
    ==========
    St : float
        stock/index level at time t
    K : float
        strike price
    T : float
        date of maturity/time-to-maturity if t = 0; T > t
    r : float
        constant, risk-less short rate
    sigma : float
        volatility

    Returns
    =======
    put_value : float
        European put present value at t
    '''
    put_value = bsm_call_value(S0, K, T, r, sigma) \
        - S0 + math.exp(-r * T) * K
    return put_value


def vasicek_zcb_value(T, al, mu, sigma, r0):
    
    '''
    Calculates zcb $P(0, T)$ given vasicek mdoel with
    model parameters
        al, mu, sigma, r0
    '''
    
    B = (1 - np.exp(-al*T))/al
    A = (B - T)*(mu - sigma**2/2/al**2) - sigma**2/4/al*B**2
    
    P = np.exp(A - B*r0)
    return P

def vasicek_libor_rate(T, al, mu, sigma, r0):
    '''
    Calculates Libor rate $L(0, T)$ given vasicek mdoel with
    model parameters
        al, mu, sigma, r0
    '''
    P = vasicek_zcb_value(T, al, mu, sigma, r0)
    L = 100/T*(1/P - 1)
    return L

    
def vasicek_swap_rate(T, N, al, mu, sigma, r0):
    delta = T/N
    PP = np.zeros(N) #store zcb prices
    for i in range(N):
        PP[i] = vasicek_zcb_value((i+1)*delta, al, mu, sigma, r0)

    S = 100*(1 - PP[-1])/delta/np.sum(PP)
    return S    
    
    

if __name__ == "__main__":
    
    #vasicek model parameter
    th = [.1, .05, .003, .03]
    al, mu, sigma, r0 = th
    
    print('vasicek model is given as ' + str(th))
    
    print('zcb P(0,1) is ' + str(vasicek_zcb_value(1, al, mu, sigma, r0)))
    
    print('Libor L(0,1) is ' + str(vasicek_libor_rate(1, al, mu, sigma, r0)))
    
    
    
    