a=list(map(int,input().split()))
n, m ,k = a[0],a[1],a[2]
g = dict()
for i in range(n):
    g[i]=[]
for i in range(m):
    b = list(map(int, input().split()))
    q = b[0]-1
    w = b[1]-1
    g[q].append(w)
    g[w].append(q)
s = [0]*k
for i in range(k):
    c = list(input().split())
    s[i] = [c[0],c[1],c[2]]

def dfsvisit(graph,nod,color,visited):
    stack = [nod]
    while stack:
        node = stack.pop(-1)
        color[node] = 1
        visited.append(node)
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                stack.append(neighbour)
                color[neighbour]=1
        color[node] = 2

def kosaraju(graph):
    comps=[]
    ts = [i for i in range(n)]
    color = [0 for i in graph]
    while ts:
        node = ts[0]
        component = []
        dfsvisit(graph,node,color,component)
        comps.append(component)
        for node in component:
            ts.remove(node)
    return comps

def kosupdate(graph,comps,l):
    for h in range(len(comps)):
        if l in comps[h]:
            ts = [i for i in comps[h]]
            comps.remove(comps[h])
            break
    color = [0 for i in graph]

    while ts:
        node = ts[0]
        component = []
        dfsvisit(graph, node, color, component)
        comps.append(component)
        for node in component:
            ts.remove(node)
    return comps


comps = kosaraju(g)
for i in range(k):
    if s[i][0] == 'cut':
        g[int(s[i][1])-1].remove(int(s[i][2])-1)
        g[int(s[i][2])-1].remove(int(s[i][1])-1)
        comps = kosupdate(g,comps,int(s[i][1])-1)
    else:
        d=0
        for j in range(len(comps)):
            if int(s[i][1])-1 in comps[j] and int(s[i][2])-1 in comps[j]:
                d+=1
        if d==0:
            print('NO')
        else:
            print('YES')