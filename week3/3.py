c=list(map(int, input().split()))
d=0
k=0
ma=max(c)
mi=min(c)
print(c, ma, mi)
while True:
    if max(c)%min(c)==0:
        d=min(c)
        break
    else:
        mi = (max(c)%min(c))
        max(c)==mi
    print(max(c))
print(d)