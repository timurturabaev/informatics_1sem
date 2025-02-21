a = list(input().split())
l=len(a)
b=[0]*l
b1=[]
c=[0]*l
le=len(a[0])

def translate(n):
    r=a[n]
    m=[]
    for i1 in r:
        m.append(ord(i1))
    return m

for i in range(l):
    b[i]=translate(i)
    b1.append(translate(i))

def sort(p):
    if len(p) <= 1:
        return p
    reference = p[len(p) // 2]
    small = [number for number in p if number < reference]
    equal = [number for number in p if number == reference]
    big = [number for number in p if number > reference]
    return sort(small) + equal + sort(big)

for i in range(l):
    c[i]=sort(b1[i])

d=[]
for i in range(l):
    d.append(c.count(c[i]))

z=0
w=1
while w>0:
    w=0
    for i in range(l-1-z):
        if d[i]<d[i+1]:
            d[i],d[i+1]=d[i+1],d[i]
            a[i],a[i+1]=a[i+1],a[i]
            b[i], b[i + 1] = b[i + 1], b[i]
            c[i], c[i + 1] = c[i + 1], c[i]
            w+=1
    z+=1

z=0
w=1
while w>0:
    w=0
    for i in range(l-1-z):
        if d[i]==d[i+1]:
            for k in range(le):
                if b[i][k]<b[i+1][k]:
                    break
                elif b[i][k]>b[i+1][k]:
                    d[i],d[i+1]=d[i+1],d[i]
                    a[i],a[i+1]=a[i+1],a[i]
                    b[i], b[i + 1] = b[i + 1], b[i]
                    c[i], c[i + 1] = c[i + 1], c[i]
                    w+=1
                    break
                else:
                    continue
    z+=1

for i in range(l):
    print(a[i],end=' ')
#time limit(