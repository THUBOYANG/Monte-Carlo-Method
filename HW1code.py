#(2)
def permutation(m,n):
    ans = 1
    for i in range(m-n+1,m+1):
        ans *= i
    return ans

for i in range(1,366):
    if permutation(365,i)/365**i < 1/2:
        print(i)
        break

#(3)
ans = 0
for i in range(1,367):
    ans += i*(permutation(365,i-1)/365**(i-1)-permutation(365,i)/365**(i))
print(ans)

#simulation

import time
import random
a1=(2018,1,1,0,0,0,0,0,0)       #start date and time
a2=(2018,12,31,23,59,59,0,0,0)  #end date and time
start=time.mktime(a1)
end=time.mktime(a2)
N = []
n = 10000 # simulation times
for k in range(n):
    birth = []
    signal = 0
    for i in range(366):
        t=random.randint(start,end)  
        date_touple=time.localtime(t)     
        date=time.strftime("%Y-%m-%d",date_touple) 
        birth.append(date)
        if i > 0:
            for j in range(len(birth)-1):
                if birth[j] == date:
                    N.append(i+1)
                    signal = 1
                    break
        if signal == 1:
            break
print(sum(N)/n)