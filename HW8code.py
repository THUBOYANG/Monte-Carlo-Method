import numpy as np

def MCRSM(N, P, C):
    count = 0
    MC = [1]
    t = np.zeros(N)
    R = np.zeros(N)
    while count<N:
        r = np.random.uniform(0,1)
        if r <= P[MC[-1]-1,0]:
            MC.append(1)
            R[count] += C[MC[-1]-1,0]
            t[count] += 1
        else:
            MC.append(2)
            R[count] += C[MC[-1]-1,1]
            t[count] += 1
        if MC[-1] == 1:
            count += 1
    return t,R

if __name__ == '__main__':
    N = 1000
    P = np.array([[1/3,2/3],[1/4,3/4]])
    C = np.array([[0,1],[2,3]])
    t,R = MCRSM(N,P,C)
    l = np.mean(R)/np.mean(t)
    S_2 = np.cov(R,t)[0,0]-2*l*np.cov(R,t)[0,1]+l**2*np.cov(R,t)[1,1]
    left = l - 1.96*np.sqrt(S_2)/np.mean(t)/np.sqrt(N)
    right = l + 1.96*np.sqrt(S_2)/np.mean(t)/np.sqrt(N)
    print('The point estimate of l is %.4f'%l)
    print('The 95%% confidence interval of l is (%.4f,%.4f)'%(left,right))
    