# 18ma573v01 

## COMPUTATIONAL METHODS OF FINANCIAL MATHEMATICS

__General course info__

- Syllabus - [pdf](doc/syllabus_v01.pdf)
- Final and capston project -[pdf](./doc/capstone.pdf)

__Python basics on Jupyter notebook__

In this section, we will get familiar with python language with Jupyter notebook through some financial applications.

- Environment setup [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/first_notebook_v01.ipynb)
- Python on Jupyter notebook [ipynb](src/python_notebook.ipynb)
- Pandas [ipynb](src/pandas_basics.ipynb)

__Finite difference operators with python functions__

Below, we will discuss some simple coding related to finite difference operators and convergence rate. This will help you to get to know basic coding with python functions. However, it's your responsibility to get to know enough coding via online resource. 

- First order finite difference operators - [ipynb](src/first_fd_v01.ipynb)
- Convergence order - [ipynb](src/ffd_convergence_rate_v01.ipynb)
    - (hw) Second order finite difference operator - [ipynb](src/second_fd.ipynb) 
        - soln - [ipynb](src/second_fd_soln.ipynb)
    - (hw) Finite difference operator with higher order convergence - [ipynb](src/ex_fd.ipynb)
        - soln - [ipynb](src/ex_fd_soln.ipynb)
    - (ex) FD - [ipynb](doc/fd_ex.pdf)


__BSM option price__

- European call/put option class - 
    [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/european_options_class.ipynb)
    - (hw) payoff diagram of butterfly - 
        [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/option_combinations.ipynb)
- BSM formula - 
    [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/bsm_formula_v01.ipynb)
    - (hw) Bsm price change -
        [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/bsm_price_change.ipynb)
- Importing modules - 
    [md](https://github.com/songqsh/18ma573pub/blob/master/src/import_modules.md)
    
__Calibration__

- implied volatility - [ipynb](https://nbviewer.jupyter.org/github/songqsh/18ma573pub/blob/master/src/implied_vol_v01.ipynb)
    - (hw) IV - [ipynb](https://nbviewer.jupyter.org/github/songqsh/18ma573pub/blob/master/src/hw_implied_vol.ipynb)
- volatility smile  - [ipynb](https://nbviewer.jupyter.org/github/songqsh/18ma573pub/blob/master/src/vol_smile.ipynb)
- bsm_calibration - [ipynb](https://nbviewer.jupyter.org/github/songqsh/18ma573pub/blob/master/src/bsm_calibration.ipynb)
    
    
__Monte Carlo basics__

- Monte Carlo basics: Estimating $\pi$ - [pdf](./doc/pi_mc_01.pdf) - [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/pi.ipynb)
    - (hw) [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/hw_mc_01.ipynb)
    - (hw) [ipynb](https://github.com/songqsh/18ma573pub/blob/master/src/hw_mc_02.ipynb)
- Ordinary Monte Carlo: Definite integral [pdf](https://github.com/songqsh/18ma573pub/blob/master/doc/omc_integral_01.pdf)
    - (hw) [pdf](https://github.com/songqsh/18ma573pub/blob/master/doc/hw_omc_integral.pdf)
    
__Exact sampling__    
- [Exact sampling of Brownian motion](./src/bm_1d.ipynb)
    - [Prj: BSM + exact value + exact sampling](./doc/omc_integral_prj.pdf)
- [Inverse transform method + Importance sampling: Definite integral](./doc/is_it_integral.pdf)

__Euler scheme__
- 1d Euler scheme - [pdf](./doc/euler_sde_1d.pdf)
    - Demo: bm_1d_path - [ipynb](./src/bm_1d_path.ipynb)
    - Demo: euler_1d_path - [ipynb](./src/euler_1d.ipynb)
- 2d Euler scheme - [pdf](./doc/euler_sde_2d.pdf)
    - Call on Heston model - [ipynb](./src/euler_heston.ipynb)
    - Heston European option data cook - [ipynb](./src/heston_data_cook.ipynb)
    
__Path dependent otpions__
- BSM geometric asian option 
- Path class - [ipynb](./src/path_nd_v01.ipynb)
    
__Finite difference method__    
- [Demonstration of Stability for FTCS](./doc/stability_ftcs_01.pdf)
- [Stability analysis of FTCS](./doc/stability_ftcs_02.pdf)
- [Crank-Nicolson scheme](./doc/stability_ftcs_03.pdf)


# Explicit pricing formula

- [Explicit Option Price: BSM+Eu](./src/explicit_bsm_eu.ipynb)
- [Project: BSM Greeks](./src/explicit_bsm_greeks.ipynb)
    - [Soln](./src/explicit_bsm_greeks_soln.ipynb)
- [Explicit Zero Coupon price: Vasicek+Zcb](./src/explicit_vasicek_zcb.ipynb)
- [Calibration: Vasicek + Libor + Swap](./src/calibration_vasicek_libor_swap.ipynb)

# Monte Carlo - Exact sampling
- [Exact Sampling: BSM+Eu](./src/es_bsm_eu.ipynb)
- [Exact sampling: BSM + Knock-in](./src/es_bsm_knock_in.ipynb)
- [Importance sampling: BSM + Knock-in](./src/is_bsm_knock_in.ipynb)
- [Control Variates: BSM+Aac](./src/control_variates_bsm_aac.ipynb)


# Finite difference method
- FTCS with a toy - [ipynb](src/ftcs_stability_heat_toy.ipynb)
    - (hw) FTCS stability questions - [ipynb](src/hw_ftcs_stability.ipynb)
- BTCS and CRR model - [pdf](doc/fdm_crr.pdf)
    - (hw) [pdf](doc/hw_crr.pdf)
    - (soln by) [song](https://github.com/songqsh/MA6628v02/blob/master/L05s01.ipynb)
- FTCS and stability: Heat equation with Cauchy-Dirichlet data - [ipynb](./src/ftcs_stability_heat_1d.ipynb)
- BTCS and stability: Heat equation - [ipynb](./src/btcs_stability_heat_1d.ipynb)


# Problem Sets

- [Problems01](./src/problems01.ipynb)
    


=======================================

[Start here](startpage.ipynb)
