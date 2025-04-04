# Final project guidelines

The final project should be done in a group of 2-3 people, and independently uploaded to your GitHub at last. Your analytic (non-coding) part shall be strictly in the range of 3-8 pages. 

- The topic could be from any problems from the class and in-depth investigation is needed for a satisfactory credit. For instance, extended studies with real market data on the discusssion of the homework problem [here](20bsm_calibration_v01hw.ipynb) could be appropriate.
- Alternatively, you can recover some numerical results from the existing literature either by methods provided by the reference or learned from class. 

To get high grade, it is crucial to include your "new findings" either from some empirical conclusion or theoretical conclusion, as long as it has not been discussed in our class. If you could replicate an idea or observation from some existing literature not covered by class, we still count this as your "new findings".
Be creative and look forward to your new findings!


# References

## Books
- C. Fries, Mathematical Finance: Theory, Modeling, Implementation. Wiley, 2007
- Paul Glasserman, Monte Carlo Methods in Financial Engineering. Springer 2004.
  - Page 267-Table4.4: Konck-in barrier options with IS
  - Page 272-Table4.5: Asian options with IS
- Ali Hirsa, Computational Methods in Finance. Chapman Hall/CRC 2013.
  - Page 163, Table 4.1-4.2: Vanilla option under Heston
## Papers
- Dereich, Neuenkirch, and Szpruch, An Euler-type method for the strong approximation of the Cox–Ingersoll–Ross process, 2011 [pdf](https://github.com/songqsh/songqsh.github.io/blob/master/paper/11DNS_euler_cir.pdf)
  - This paper proposes euler method after squared transformation, which is different from the conventional truncation method.
  - Strong convergence order is shown 1/2.
- Longstaff and Schwartz, Valuing American Options by Simulation: A Simple Least-Squares Approach, The review of financial studies, 2001, [pdf](https://github.com/songqsh/songqsh.github.io/blob/master/paper/01LSAmericanOption.pdf)
  - This paper provides a least square method of American option pricing. 
  - Table 1: American options underlying bs model with LS.
---
- Wenhao Qiu, Qingshuo Song, George Yin, Solving Elliptic Hamilton-Jacobi-Bellman Equations in A Value Space, 2020, [pdf](https://github.com/songqsh/songqsh.github.io/blob/master/paper/20QSYepdenum.pdf)
  - This paper studies value iteration and deep learning approach on the MDP approximating elliptic HJB.
  - Deep learning approach is not sufficiently stable. In principle, one can use any reinforcement learning technique on MDP other than value iteration, which is described as the future work.
- Qingshuo Song, Convergence of Markov chain approximation on generalized HJB equation and its applications, 2008, [pdf](https://github.com/songqsh/songqsh.github.io/blob/master/paper/08Son-Auto.pdf)
  - This paper studies MDP approximation for parabolic HJB.
  - No numerical computation is given in this paper.
- Qingshuo Song, George Yin, Zhimin Zhang, AN epsilon-UNIFORM FINITE ELEMENT METHOD FOR SINGULARLY PERTURBED BOUNDARY VALUE PROBLEMS, [pdf](https://github.com/songqsh/songqsh.github.io/blob/master/paper/07SYZ-FEM.pdf)
  - This paper studies epsilon uniform finite element method
  - It improves efficiency of FEM using two interpolations.
