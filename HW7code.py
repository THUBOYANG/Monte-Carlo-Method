import numpy as np
from scipy.integrate import quad

#4.1
N=100
H1 = []
H2 = []
for i in range(N):
    H1.append(4*np.exp(-np.random.uniform(-2,2)**2/2))
    H2.append(np.sqrt(2*np.pi)*(np.abs(np.random.normal(0,1))<=2))
#(a)
l_1_estimate = np.mean(H1)
l_2_estimate = np.mean(H2)
print('The estimated l by (A) is %.4f'%l_1_estimate)
print('The estimated l by (B) is %.4f'%l_2_estimate)
#(b)
re_error1 = np.std(H1)/np.sqrt(N)/np.mean(H1)
re_error2 = np.std(H2)/np.sqrt(N)/np.mean(H2)
print('The estimated relative error for (A) is %.4f'%re_error1)
print('The estimated relative error for (B) is %.4f'%re_error2)

#(c)
left_1 = l_1_estimate-1.96*np.std(H1)/np.sqrt(100)
right_1 = l_1_estimate+1.96*np.std(H1)/np.sqrt(100)
left_2 = l_2_estimate-1.96*np.std(H2)/np.sqrt(100)
right_2 = l_2_estimate+1.96*np.std(H2)/np.sqrt(100)
print('The 95%% confidence interval for (A) is (%.4f,%.4f)'%(left_1,right_1))
print('The 95%% confidence interval for (B) is (%.4f,%.4f)'%(left_2,right_2))
#(d)
N1 = 3874009
N2 = 475155
HN1 = [4*np.exp(-np.random.uniform(-2,2)**2/2) for i in range(N1)]
HN2 = [np.sqrt(2*np.pi)*(np.abs(np.random.normal(0,1))<=2) for i in range(N2)]
lN1_estimate = np.mean(HN1)
lN2_estimate = np.mean(HN2)
l = quad(lambda x:np.exp(-x**2/2),-2,2)[0]
print('The estimated value of l with method(A) is %.4f'%lN1_estimate)
print('The estimated value of l with method(B) is %.4f'%lN2_estimate)
print('The true value of l is %.4f'%l)
