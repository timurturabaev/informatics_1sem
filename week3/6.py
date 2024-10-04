import numpy as np
import matplotlib.pyplot as plt
n=int(input())
x = np.zeros((1,n))
x[0]=input().split()
y = np.zeros((1,n))
y[0]=input().split()
xya=0
xa=0
ya=0
x2a=0
for i in range(n):
    xya+=x[0,i]*y[0,i]
    xa+=x[0,i]
    ya+=y[0,i]
    x2a+=(x[0,i])**2
xya=xya/n
xa=xa/n
ya=ya/n
x2a=x2a/n
print(xya,xa,ya,x2a)
k=(xya-xa*ya)/(x2a-xa**2)
b=ya-k*xa
print('k =', k,'b =', b)


xm=-999
ym=-999
for i in range(n):
    if x[0,i]>xm:
        xm=x[0,i]
    if y[0,i]>ym:
        ym=y[0,i]

xmi=999
ymi=999
for i in range(n):
    if x[0,i]<xmi:
        xmi=x[0,i]
    if y[0,i]<ymi:
        ymi=y[0,i]

plt.figure(figsize=(8,16))

#b=0
xt=1
yt=1
xn=0
yn=0
#xn=round(xmi)-xt
#yn=round(ymi)-xt

x1=np.arange(xn,round(xm)+2*xt)
plt.plot(x1,k*x1+b, lw='2', color='red')
plt.plot(x,y, marker='+', linestyle='', lw='3', color='black')

plt.xticks(np.arange(xn,round(xm)+xt,xt))
plt.yticks(np.arange(yn,round(ym)+yt,yt))
plt.show()