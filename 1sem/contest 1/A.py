a=list(map(int, input().split()))
n=a[0]
k=a[1]
p=2*k+2
b=[0]*p+[0]*n*k
b[p]=1
if (n+k-2)%3==0 and max(n,k)<2*min(n,k):
    for i in range(p,n*k+p):
        b[i]+=b[i-k-2]
        b[i]+=b[i-2*k-1]
    print(b[n*k+p-1])
else:
    print(0)