t=int(input())

def sv(g):
    mincut=9**9
    for w in range(m-1):
        a = phase(g)
        if a<mincut:
            mincut=a
    return mincut

def merge(g,x1,y1):
    n=len(g)
    x=min(x1,y1)
    y=max(x1,y1)
    for k in range(n):
        zxc=g[k][y]
        if k!=x:
            g[k][x]+=zxc
            g[x][k]+=zxc
    for k in range(n):
        g[k][y]=10
        g[k].remove(10)
    g.remove(g[y])
    return

def phase(g):
    n=len(g)
    v=[]
    v.append(0)
    while len(v)!=len(g):
        ma = 0
        for i in v:
            for j in range(n):
                if j not in v and g[i][j] > ma:
                    ma=g[i][j]
                    u = j
        v.append(u)
    x1=v[-1]
    y1=v[-2]
    currentcut=min(sum(g[x1]),sum(g[y1]))
    merge(g,x1,y1)
    return currentcut

ans=[]

for i in range(t):
    g=[]
    m=int(input())
    n=m
    for j in range(n):
        z=input()
        x=[]
        for k in z:
            x.append(int(k))
        g.append(x)
    ans.append(sv(g))

for i in range(t):
    print(ans[i])