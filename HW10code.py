import numpy as np
import scipy.stats as stats

def AR(a,b,n,N):
    X = np.zeros((N,n))
    total_num = 0
    c = 2.0736
    for i in range(N):
        np.random.seed(i)
        count = 0
        while count < n:
            u = np.random.uniform(0,1)
            x = np.random.uniform(0,1)
            if u <= stats.beta.pdf(x,a,b)/c:
                X[i,count] = x
                count += 1
            total_num += 1
    return X, N*n/total_num

def MH(a,b,n,N):
    X = np.zeros((N,n+1))
    accept_num = 0
    X[:,0] = 0.5
    for i in range(N):
        np.random.seed(i)
        count = 0
        while count < n:
            u = np.random.uniform(0,1)
            w = np.random.uniform(0,1)
            alpha = min(stats.beta.pdf(w,a,b)/stats.beta.pdf(X[i,count],a,b),1)
            if u <= alpha:
                X[i,count+1] = w
                accept_num += 1
            else:
                X[i,count+1] = X[i,count]
            count += 1
    return X[:,1:], accept_num/(n*N)

if __name__ == '__main__':
    X_AR,accept_rate_AR = AR(4,3,50,500)
    X_MH,accept_rate_MH = MH(4,3,500,500)
    burn_in = 450
    #(a)
    print('The accept rate of AR method is %.4f'%accept_rate_AR)
    print('The accept rate of MH method is %.4f'%accept_rate_MH)
    #(b)
    bias_sample_mean_AR = np.array([np.abs(np.mean(X_AR[i,:])-4/7) for i in range(500)])
    bias_sample_mean_MH = np.array([np.abs(np.mean(X_MH[i,burn_in:])-4/7) for i in range(500)])
    stats.ttest_ind(bias_sample_mean_AR, bias_sample_mean_MH, equal_var = False)


    
    
            