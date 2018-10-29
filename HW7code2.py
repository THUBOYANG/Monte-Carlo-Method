import numpy as np

#4.8
#(a)
enter = [0] #the arriving time of each person
leave = [0] #the leaving time of each person
X = [0] #the number of people at each time
T = 10000

while enter[-1]<T:
    enter.append(enter[-1]+np.random.exponential(1))
    
leave.append(enter[1]+np.random.exponential(1/2))
i=2
while i<len(enter) and leave[-1]<T:
    leave.append(max(leave[-1],enter[i])+np.random.exponential(1/2))
    i += 1
for t in range(1,T+1):
    position = len([k for k in enter if k<=t])-len([k for k in leave if k<=t ])
    X.append(position)
N=30
T_batch = int((T-100)/N)
Y_batch = []
X_for_batch = X[101:]
for k in range(N):
    Y_batch.append([j for j in X_for_batch[k*T_batch:(k+1)*T_batch]])
Y = [np.mean(Y_batch[k]) for k in range(N)]
l_batch = np.mean(Y)
left_batch = l_batch-1.96*np.std(Y)/np.sqrt(N)
right_batch = l_batch+1.96*np.std(Y)/np.sqrt(N)
print('The point estimate for l with batch method is %.4f'%l_batch)
print('The 95%% confidence interval of batch method is (%.4f,%.4f)'%(left_batch,right_batch))
    
#(b)
re_index = []
R_re = []
t_re = []
for i in range(T):
    if X[i]==0 and X[i+1]!=0:
        re_index.append(i+1)
re_index.append(T+1)
for i in range(len(re_index)-1):
    R_re.append(sum(X[re_index[i]:re_index[i+1]]))
    t_re.append(re_index[i+1]-re_index[i])
l_re = np.mean(R_re)/np.mean(t_re)
left_re = l_re-1.96*np.sqrt(np.var(R_re)-2*l_re*np.cov(R_re,t_re)[0][1]+l_re**2*np.var(t_re))/np.mean(t_re)/np.sqrt(len(R_re))
right_re = l_re+1.96*np.sqrt(np.var(R_re)-2*l_re*np.cov(R_re,t_re)[0][1]+l_re**2*np.var(t_re))/np.mean(t_re)/np.sqrt(len(R_re))
print('The point estimate for l with regenerative method is %.4f'%l_re)
print('The 95%% confidence interval of regenerative method is (%.4f,%.4f)'%(left_re,right_re))

    