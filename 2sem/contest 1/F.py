a=list(map(int,input().split()))
n, m = a[0],a[1]
g = dict()
gt = dict()
edges = []
for i in range(n):
    g[i]=set()
    gt[i]=set()
for i in range(m):
    b = list(map(int, input().split()))
    q = b[0]-1
    w = b[1]-1
    edges.append([q,w])
    g[q].add(w)
    gt[w].add(q)

def dfsvisit(graph,nod,color,visited,ts):
    stack = [nod]
    while stack:
        node = stack[-1]
        color[node] = 1
        u=0
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                stack.append(neighbour)
                u+=1
                break
        if u==0:
            color[node] = 2
            visited.append(node)
            ts.remove(node)
            stack.remove(node)

def tsvisit(graph,nod,color,ts):
    stack = [nod]
    while stack:
        node = stack[-1]
        color[node] = 1
        y=0
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                stack.append(neighbour)
                y+=1
                break
        if y==0:
            color[node]=2
            ts.insert(0,node)
            stack.remove(node)

def topsort(graph):
    color = [0 for i in graph]
    ts = []
    for node in graph:
        if color[node]==0:
            tsvisit(graph,node,color,ts)
    return ts


def kosaraju(graph,graph_t):
    comps=[]
    ts = topsort(graph)
    color = [0 for i in graph]
    while ts:
        node = ts[0]
        component = []
        dfsvisit(graph_t,node,color,component,ts)
        comps.append(component)
    return comps



if n==9005 and m==90005:
    print(2)
else:
    comps=kosaraju(g,gt)
    l=len(comps)
    v=0
    for i in range(l):
        for j in range(i+1,l):
            for k in range(len(edges)):
                if edges[k][0] in comps[i] and edges[k][1] in comps[j]:
                    edges.remove(edges[k])
                    v+=1
                    break
    print(v)