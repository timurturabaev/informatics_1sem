#g=[]
#n=int(input())
#for k in range(n):
#    g.append(list(map(int,input().split())))

gr=[[0,1,0,2],
    [1,0,0,4],
    [0,0,0,3],
    [2,4,3,0]]
n=len(gr[0])

def prim(g):
    mst = []
    s=set()
    v=0
    s.add(v)
    sum=0
    while len(s)<n:
        min=9**99
        for i in s:
            for j in range(n):
                if j not in s and g[i][j]!=0 and g[i][j]<min:
                    min=g[i][j]
                    v=i
                    u=j
        mst.append([v,u])
        s.add(u)
        sum+=g[v][u]
    print(sum)
    return mst

print(prim(gr))