a=list(map(int,input().split()))
n, m = a[0],a[1]
g = dict()
gt = dict()
edges = []
inedge=[0]*n
for i in range(n):
    g[i]=[]
    gt[i]=[]
for i in range(m):
    b = list(map(int, input().split()))
    q = b[0]-1
    w = b[1]-1
    edges.append([q,w])
    inedge[w]+=1
    g[q].append(w)
    gt[w].append(q)

def tsvisit(graph,nod,color,ts):
    stack = [nod]
    while stack:
        node = stack[-1]
        color[node] = 1
        y = 0
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                stack.append(neighbour)
                y += 1
                break
        if y == 0:
            color[node] = 2
            ts.insert(0, node)
            stack.remove(node)

def topsort(graph):
    color = [0 for i in graph]
    ts = []
    for node in graph:
        if color[node]==0:
            tsvisit(graph,node,color,ts)
    return ts

s=[]
for i in range(n):
    if inedge[i]==0:
        s.append(i)


c=0
q=0
while len(s)>0:
    if len(s)>1:
        q=1
    node=s.pop(0)
    c+=1
    for neighbour in g[node]:
        inedge[neighbour]-=1
        if inedge[neighbour]==0:
            s.append(neighbour)
if c<n:
    answer=-1
else:
    if q==1:
        answer='NO'
    else:
        answer='YES'

print(answer)
