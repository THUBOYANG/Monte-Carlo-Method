# -*- coding: utf-8 -*-
import numpy as np

def NonCRNestimate(N,u,h):
    X = np.random.exponential(1/(2*(u+h)),N)
    Y = np.random.exponential(1/(2*u),N)
    return X,Y,(np.mean(X)-np.mean(Y))/h

def CRNestimate(N,u,h):
    U = np.random.uniform(0,1,N)
    X = -np.log(U)/(2*(u+h))
    Y = -np.log(U)/(2*u)
    return X,Y,(np.mean(X)-np.mean(Y))/h

if __name__ == '__main__':
    u = 1
    h = .01
    N = 10**6
    true_value = -1/2
    X,Y,NonCRN_estimator = NonCRNestimate(N,u,h)
    X_CRN,Y_CRN,CRN_estimator = CRNestimate(N,u,h)
    NonCRN_rel_error = np.std((X-Y)/h)/np.sqrt(N)/NonCRN_estimator
    CRN_rel_error = np.std((X_CRN-Y_CRN)/h)/np.sqrt(N)/CRN_estimator
    print('The estimator of NonCRN is %.4f and its relative error is %.4f'%(NonCRN_estimator,NonCRN_rel_error))
    print('The estimator of CRN is %.4f and its relative error is %.4f'%(CRN_estimator,CRN_rel_error))
    

    
