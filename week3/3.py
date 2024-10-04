c=list(map(int, input().split()))
a=c[0]
b=c[1]
ma=max(c)
mi=min(c)
while mi>0:
    k=ma%mi
    if k==0:
        d=mi
        break
    else:
        mi,ma = k,mi
x1=b
y1=-a+d/b
for i in range(b):
    x=i
    y=(d-a*x)/b
    if round(y)-y==0:
        if abs(x)+abs(y)<abs(x1)+abs(y1):
            if abs(x)<abs(x1):
                x1=x
                y1=y
    x=-i
    y=(d-a*x)/b
    if round(y)-y==0:
        if abs(x)+abs(y)<abs(x1)+abs(y1):
            if abs(x)<abs(x1):
                x1=x
                y1=y
print(int(x1),int(y1),d)