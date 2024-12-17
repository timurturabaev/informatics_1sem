k = int(input())
test=[0]*k
n=[]
m=[]
inum=[]
for i3 in range(k):
    a = list(map(int, input().split()))
    n.append(a[0])
    m.append(a[1])
    inum.append([0]*m[i3])
    b = []
    for j3 in range(m[i3]):
        c=input()
        b.append(c)
    test[i3]=b
d=test.copy()
def translate(x,y):
    p=d[x][y]
    r=[]
    for w in p:
        if w=='A':
            r.append(1)
        elif w=='C':
            r.append(2)
        elif w=='G':
            r.append(3)
        else:
            r.append(4)
    return r

def inverse(r):
    l=len(r)
    kol=0
    if l<=1:
        return kol
    for i1 in range(l):
        value=r[i1]
        for j1 in range(1,l-i1):
            if i1+j1<l:
                if value>r[i1+j1]:
                    kol+=1
    return kol

for i2 in range(k):
    for j2 in range(m[i2]):
        inum[i2][j2]=inverse(translate(i2,j2))

w=1
while w>0:
    w=0
    for i in range(k):
        for j in range(m[i]-1):
            if inum[i][j]>inum[i][j+1]:
                inum[i][j],inum[i][j+1]=inum[i][j+1],inum[i][j]
                test[i][j],test[i][j+1]=test[i][j+1],test[i][j]
                w+=1

for i4 in range(k):
    for j4 in range(m[i4]):
        print(test[i4][j4],end='\n')
    if i4+1<k:
        print('\n',end='')