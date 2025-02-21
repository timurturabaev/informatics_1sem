a = list(map(int, input().split()))
l=len(a)+1
b=[a[0]]+a
r=0
def high(n):
    global r
    for i in range(1,n):
        if b[n-i]>=b[n]:
            r=n-i-1
            break
        else:
            r=-1
    return r
print(-1,end=' ')
for j in range(2,l):
    print(high(j),end=' ')