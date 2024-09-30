a = list(map(int, input().split()))
c=1
m=0
n=0
for i in range(len(a)):
    c=a.count(a[i])
    if c>=m:
        m=c
        n=a[i]
print(n)