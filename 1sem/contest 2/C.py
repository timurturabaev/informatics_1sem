a = list(map(int, input().split()))
l=len(a)
b=[]
def chain(n):
    value=a[n]
    k=0
    if l<=1:
        return k
    for i in range(1,l-n):
        if i+n<l:
            if value<a[i+n]:
                k+=1
                value=a[i+n]
    return k
for j in range(l):
    b.append(chain(j))
for j in range(l):
    print(b[j],end=' ')