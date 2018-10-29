# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:44:08 2018

@author: Li Boyang
"""

import numpy as np
from scipy.integrate import quad
import random as rd 

def MonteCarloIntegration(n,a,b):
    value = []
    for i in range(0,n):
        x = rd.uniform(a,b)
        value.append(np.exp(-x**2/2))
    return sum(value)*(b-a)/n

def main():
    #(a)
    s1,err1 = quad(lambda x: np.exp(-x**2/2),0,1)
    s2,err2 = quad(lambda x: np.exp(-x**2/2),0,4)
    print('a = 0, b = 1, true integral value = %.3f' %(s1))
    print('a = 0, b = 4, true integral value = %.3f' %(s2))
    #(b)
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(20,0,1,MonteCarloIntegration(20,0,1)))
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(20,0,4,MonteCarloIntegration(20,0,4)))
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(200,0,1,MonteCarloIntegration(200,0,1)))
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(200,0,4,MonteCarloIntegration(200,0,4)))
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(2000,0,1,MonteCarloIntegration(2000,0,1)))
    print('n = %d, a = %d, b = %d, estimate of integral = %.3f' %(2000,0,4,MonteCarloIntegration(2000,0,4)))
    
if __name__ == '__main__':
    main()