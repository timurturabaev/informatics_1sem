import numpy as np
n = int(input())
a = np.array([[[0]*n]*n])
for i in range(n):
    a[0, i]=input().split() #вводится по столбцам
b = np.array([[0]*n])
b[0]=input().split()
print(a)
print(b)
d = np.linalg.det(a)
x = []
if d != 0:
    for i in range(n):
        a1=np.copy(a)
        a1[:,i]=b
        c = np.linalg.det(a1)/d
        x.append(c)
else:
    x='zero or infinite solutions'
print(x)