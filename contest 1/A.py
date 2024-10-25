a=list(map(int, input().split()))
a=a[:2]
n=a[0]
k=a[1]
b=[[0]*k]*n
b[0][3]=1
print(b)
if (n+k-2)%3==0 and max(n,k)<2*min(n,k):
    x=1
else:
    x=0
print(x)