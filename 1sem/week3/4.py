a = input().split()
n = int(a[0])//2
i=0
while i<n:
    i+=1
    print(a[1]*i)
if int(a[0])%2==1:
    print(a[1]*(n+1))
while i>0:
    print(a[1]*i)
    i-=1