a=list(map(int, input().split()))
a=a[:2]
n=a[0]
k=a[1]
b=[[0]*k]*n
if k == 0:
    n=k
for i in range(n):
    b[i]=list(map(int, input().split()))
c=0
e=[]
d=[]
f=[0]
h=[]
p=0
for i in range(n):
    for j in range(k):
        if b[i][j]==1:
            x=min(n-i,k-j)
            for g in range(x):
                for v in range(x):
                    if b[i+g][j+v]==1:
                        c+=1
                    else:
                        break
                d.append(c)
                c=0
            for q in range(max(d)):
                for w in range(len(d)):
                    if d[w]>=q+1:
                        p+=1
                        h.append(p)
                    else:
                        p=0
                if max(h)>=q+1:
                    e.append(q+1)
                p=0
                h.clear()
            z=max(e)
            d.clear()
            e.clear()
            f.append(z)
        else:
            continue
print(max(f))