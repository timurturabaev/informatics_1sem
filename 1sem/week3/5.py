import numpy as np
n = int(input())
m = int(input())
i=1
M = np.zeros((n,m))
k=1
c=1
d=0
while k<m*n:
    for i in range(m-c):
        M[c-1-d,c-1+i-d]=k
        k+=1
    for i in range(n-c):
        M[c-1+i-d,m-c+d]=k
        k+=1
    for i in range(m-c):
        M[n-c+d,m-c+d-i]=k
        k+=1
    for i in range(n-c):
        M[n-c+d-i,c-1-d]=k
        k+=1
    c+=2
    d+=1
print(M)
for i in range(n):
    M[i]*=i+1
print(M)