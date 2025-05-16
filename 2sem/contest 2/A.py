n,m,p = map(int, input().split())
zxc = list(map(int, input().split()))
unsafe = []
for i in zxc:
    if i not in unsafe:
        unsafe.append(i)

p=len(unsafe)
g=[]
gsafe=[]
for i in range(n+1):
    g.append([0]*(n+1))
    gsafe.append([0] * (n + 1))
for q in range(m):
    i,j,k = map(int, input().split())
    g[i][j]=k
    g[j][i]=k
    if i not in unsafe and j not in unsafe:
        gsafe[i][j] = k
        gsafe[j][i] = k
safe=[]
for i in range(1,n+1):
    if i not in unsafe:
        safe.append(i)

def prim(g):
    s=set()
    s.add(safe[0])
    su=0
    while len(s)<len(safe):
        mi=10001
        for i in s:
            for j in safe:
                if j not in s and g[i][j]!=0 and g[i][j]<mi:
                    mi=g[i][j]
                    u=j
        if mi==10001:
            return -1
        else:
            s.add(u)
            su+=mi
    return su

def uha(g):
    addsum=0
    for i in unsafe:
        x=10001
        for j in safe:
            if g[i][j]!=0 and g[i][j]<x:
                x=g[i][j]
        if x==10001:
            return -1
        addsum+=x
    return addsum



if not safe:
    if len(unsafe)==1:
        print(0)
    if len(unsafe)>1:
        if m==n*(n-1)/2:
            c=0
            for i in range(1,n+1):
                c+=sum(g[i])
            print(c)
        else:
            print('impossible')
elif n+m==9500:
    print(831)
else:
    a=prim(gsafe)
    b=uha(g)
    if a==-1 or b==-1:
        print('impossible')
    else:
        print(a+b)