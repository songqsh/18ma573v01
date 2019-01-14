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
- (hw) Higher order finite difference - [ipynb](src/ex_fd.ipynb)
    - soln - [ipynb](src/ex_fd_soln.ipynb)


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
    
## Calibration

- BSM formula -  [ipynb](src/bsm_formula.ipynb)
- volatility smile  - [ipynb](src/implied_vol.ipynb)
- bsm_calibration - [ipynb](src/bsm_calibration.ipynb)
    
    
## Monte Carlo basics

- [Monte Carlo basics: Estimating $\pi$](./doc/pi_mc_01.pdf)
- [Ordinary Monte Carlo: Definite integral](./doc/omc_integral.pdf)
- [Exact sampling of Brownian motion](./src/bm_1d.ipynb)
    - [Prj: BSM + exact value + exact sampling](./doc/omc_integral_prj.pdf)
- [Inverse transform method + Importance sampling: Definite integral](./doc/is_it_integral.pdf)
- 1d Euler scheme - [pdf](./doc/euler_sde_1d.pdf)
    - Demo: bm_1d_path - [ipynb](./src/bm_1d_path.ipynb)
    - Demo: euler_1d_path - [ipynb](./src/euler_1d.ipynb)
- 2d Euler scheme - [pdf](./doc/euler_sde_2d.pdf)
    - Call on Heston model - [ipynb](./src/euler_heston.ipynb)
    - Heston European option data cook - [ipynb](./src/heston_data_cook.ipynb)
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
- [FTCS and stability: Heat equation](./src/ftcs_stability_heat_1d.ipynb)
- [BTCS and stability: Heat equation](./src/btcs_stability_heat_1d.ipynb)


# Problem Sets

- [Problems01](./src/problems01.ipynb)
    


=======================================

[Start here](startpage.ipynb)
