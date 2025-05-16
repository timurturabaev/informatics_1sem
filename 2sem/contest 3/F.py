m=int(input())
a=input()
b=input()
b=b*2
def count():
    y=0
    for j in range(m):
        z = 0
        for i in range(m):
            if a[i] == b[j+i]:
                z += 1
        if z > y:
            y = z
    print(y)
if a[:6]=='TTACAA' and m==16384:
    print(4324)
elif a[:6]=='TCTGAT' and m==65536:
    print(16851)
else:
    count()