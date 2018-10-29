#Problem B
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

def EMmethod(n):
    mu = 1
    sigma = 0.2
    h = 1/n
    Y = [1]
    for i in range(1,n+1):
        Y.append(Y[i-1]*(1+mu*h+sigma*np.sqrt(h)*np.random.normal(0,1)))
    return Y

if __name__ == '__main__':
    t_1 = [t/10000 for t in range(10001)]
    t_2 = [t/10 for t in range(11)]
    Y_1_at_1 = []
    Y_2_at_1 = []
    for i in range(100):
        Y_1 = EMmethod(10000)
        Y_2 = EMmethod(10)
        Y_1_at_1.append(Y_1[10000])
        Y_2_at_1.append(Y_2[10])
        if i<3:
            plt.subplot(121)
            plt.title('h=.0001')
            plt.xlabel('t')
            plt.ylabel('X_t')
            plt.plot(t_1,Y_1)
            plt.plot(t_1,np.exp(np.array(t_1)*(1-0.04/2)),'r--')
            plt.subplot(122)
            plt.title('h=.1')
            plt.xlabel('t')
            plt.plot(t_2,Y_2)
            plt.plot(t_2,np.exp(np.array(t_2)*(1-0.04/2)),'r--')
    t_test_1 = (np.mean(Y_1_at_1)-np.exp(1-0.04/2))/(np.std(Y_1_at_1)/np.sqrt(100))
    t_test_2 = (np.mean(Y_2_at_1)-np.exp(1-0.04/2))/(np.std(Y_2_at_1)/np.sqrt(100))
    P_value_test1 = 2*t.cdf(-np.abs(t_test_1),99)
    P_value_test2 = 2*t.cdf(-np.abs(t_test_2),99)
    print('P-values for h=.0001 and h=.1 are',[P_value_test1,P_value_test2])

#Problem C
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


def EMmethodofOU(h, T):
    n = int(T/h)
    theta = 1
    mu = 20
    sigma = 10
    X = [0]
    deltaW = [0]+[np.random.normal(0,np.sqrt(h)) for i in range(n)]
    for i in range(1,n+1):
        X.append(X[i-1]+theta*(mu-X[i-1])*h+sigma*deltaW[i])
    return X

if __name__ == '__main__':
    X = np.zeros([50,501])
    for i in range(50):
        X[i] = EMmethodofOU(0.01,5)
    T = [0.01*i for i in range(501)]
    #(a)
    for i in range(5):
        plt.plot(T,X[i,:])
        plt.xlabel('t')
        plt.ylabel('X_t')
        plt.title('E-M method for O-U process')
    #(b)
    meanline = []
    for i in range(501):
        meanline.append(np.mean(X[:,i]))
    plt.plot(T,meanline)
    plt.xlabel('t')
    plt.ylabel('meanvalue')
    #(c)
    t_test_X2 = (meanline[200]-20)/(np.std(X[:,200])/np.sqrt(50))
    t_test_X5 = (meanline[500]-20)/(np.std(X[:,500])/np.sqrt(50))
    P_value_X2 = 2*t.cdf(-np.abs(t_test_X2),49)
    P_value_X5 = 2*t.cdf(-np.abs(t_test_X5),49)
    print('P_values of t-test for X(2) and X(5) are', [P_value_X2,P_value_X5])
