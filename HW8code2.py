import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #(a)
    n = 5000
    original_data = np.random.uniform(0,1,25)
    sample_mean = [np.mean([original_data[np.random.randint(0,24)] for j in range(25)]) for i in range(n)]
    plt.figure(figsize = (12,5))
    plt.subplot(1,2,1)
    z = plt.hist(sample_mean, 20, color = 'white')
    x=z[1][0:len(z[1])-1]
    y=z[0]
    plt.plot(x,y,color='b')
    plt.title('Sampling distribution')
    
    sample_mean = np.sort(sample_mean)
    bootstrap_mean = [sample_mean[int(np.ceil(np.random.uniform(0,1)*n))-1] for i in range(n)]
    plt.subplot(1,2,2)
    m = plt.hist(bootstrap_mean, 20, color = 'white')
    r=m[1][0:len(m[1])-1]
    s=m[0]
    plt.plot(r,s,color='b')
    plt.title('Bootstrap distribution')
    plt.show()
    
    #(b)
    sigma = np.sqrt(1/12/25)
    sample_mean = [i-0.5 for i in sample_mean]
    bootstrap_mean = [i-0.5 for i in bootstrap_mean]
    original_left = np.percentile(sample_mean,2.5)
    original_right = np.percentile(sample_mean,97.5)
    bootstrap_left = np.percentile(bootstrap_mean,2.5)
    bootstrap_right = np.percentile(bootstrap_mean,97.5)
    CLT_left = np.mean([x-0.5 for i in original_data])-1.96*sigma/np.sqrt(25)
    CLT_right = np.mean([x-0.5 for i in original_data])+1.96*sigma/np.sqrt(25)
    print('The 95%% confidence interval of (i) is (%.4f,%.4f)'%(original_left,original_right))
    print('The 95%% confidence interval of (ii) is (%.4f,%.4f)'%(bootstrap_left,bootstrap_right))
    print('The 95%% confidence interval of (iii) is (%.4f,%.4f)'%(CLT_left,CLT_right))