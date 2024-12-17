n=int(input())
x=[]
y=[]
for i in range(n):
    a=list(map(float, input().split()))
    y.append(a[0])
    x.append(a[1])
xya=0
xa=0
ya=0
y2a=0
for i in range(n):
    xya+=x[i]*y[i]
    xa+=x[i]
    ya+=y[i]
    y2a+=(y[i])**2
xya=xya/n
xa=xa/n
ya=ya/n
y2a=y2a/n
if y2a-ya**2==0:
    k=0
else:
    k=(xya-xa*ya)/(y2a-ya**2)
b=ya-k*xa
if k==0:
    print(1)
else:
    print(0)