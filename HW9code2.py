# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats as stats

def Standard(N,c):
    X = np.random.normal(0,1,N)
    Y = np.array([int(np.abs(X[i])>=c) for i in range(N)])
    re_error = np.std(Y)/np.mean(Y)/np.sqrt(N)
    return np.mean(Y),re_error

def IS(N,c,mu):
    X = np.random.normal(mu,1,N)
    Y = np.array([int(np.abs(X[i])>=c)*stats.norm.pdf(X[i])/stats.norm.pdf(X[i],mu,1) for i in range(N)])
    re_error = np.std(Y)/np.mean(Y)/np.sqrt(N)
    return np.mean(Y),re_error

if __name__ == '__main__':
    c = 3.5
    l_true = 2*stats.norm.cdf(-c)
    N = 20000
    mu = 3.5
    l_Standard, Standard_re_error = Standard(N,c)
    l_IS, IS_re_error = IS(N,c,mu)
    print('The true value of l is %f'%l_true)
    print('The estimator of standard method is %f and its relative error is %.4f'%(l_Standard, Standard_re_error))
    print('The estimator of IS method is %f and its relative error is %.4f'%(l_IS, IS_re_error))
    print('10 estimates l in standard way are',[Standard(N,c)[0] for i in range(10)])
    print('10 estimates l in IS are',[round(IS(N,c,mu)[0],6) for i in range(10)])

    
    
