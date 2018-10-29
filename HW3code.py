# -*- coding: utf-8 -*-
"""
@author: Li Boyang
"""
import matplotlib.pyplot as plt

def LCGs(a,c,m,x0,n):
    unif = []
    for i in range(n):
        x = (a*x0+c) % m
        unif.append(x/m)
        x0 = x
    return unif

def main():
    unif1 = LCGs(23,0,97,1,30)
    unif2 = LCGs(23,0,97,1,96)
    plt.plot(unif1[0:29], unif1[1:30], 'o')
    plt.title('U_k vs. U_k-1')
    plt.xlabel('U_k-1')
    plt.ylabel('U_k')
    plt.grid()
    plt.show()
    
    plt.plot(unif2[0:95], unif2[1:96], 'ro')
    plt.title('U_k vs. U_k-1')
    plt.xlabel('U_k-1')
    plt.ylabel('U_k')
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    main()
    