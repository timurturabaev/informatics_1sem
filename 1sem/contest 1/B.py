n=int(input())
a=[n]
b=[0]
k1=0
k2=0
k3=0
while min(a)>1:
    if a[0] % 3 == 0:
        a.append(a[0] / 3)
        k3=b[0]+1
        b.append(k3)
    if a[0] % 2 == 0:
        a.append(a[0] / 2)
        k2=b[0]+1
        b.append(k2)
    if a[0]%3!=0 and a[0]%3!=0:
        a.append(a[0] - 1)
        k1=b[0]+1
        b.append(k1)
    a.pop(0)
    b.pop(0)
print(b[-1])