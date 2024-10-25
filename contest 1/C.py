n=int(input())
a=list(map(int, input().split()))
if sum(a)%3==0:
    k=sum(a)/3
    s=3*k
    b=[]
    for i in range(n):
        b.append(a[i]%3)
else:
    print(0)
print(a)
print(b)