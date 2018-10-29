# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 01:13:46 2018

@author: Li Boyang
"""
import random as rd
import numpy as np
import matplotlib.pyplot as plt

def InverseTransform():
    U = rd.uniform(0,1)
    if U<1/4:
        X = 2*np.sqrt(U)
    else:
        X = 2*U+1/2
    return X

def AcceptanceRejection():
    U = rd.uniform(0,1)
    U0 = rd.uniform(0,1)
    X = 5/2*np.sqrt(U0)
    if X<1:
        return X
    else:
        if U <= 0.5/(0.5*X):
            return X
        else:
            return AcceptanceRejection()
    
def main():
    AcceptRej = []
    for i in range(10000):
        AcceptRej.append(AcceptanceRejection())
    plt.hist(AcceptRej, bins=40, range=(0,2.5), edgecolor = 'black')
    plt.title('A-R Method')
    
if __name__ == '__main__':
    main()
    