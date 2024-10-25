import numpy as np
n = int(input())
a = np.zeros((n,n))
for i in range(n):
    a[i]=input().split() #вводится по строкам
b = np.zeros((1,n))
b[0]=input().split()
d = np.linalg.det(a)
if d != 0:
    for i in range(n):
        a1=np.copy(a)
        a1[:,i]=b
        c=np.linalg.det(a1)/d
        print(c, end=' ')
else:
    print('zero or infinite solutions')