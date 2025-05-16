a=list(map(int,input().split()))
n,e,m=a[0],a[1],a[2]
trains=[]
stations=[]
g=dict()
for i in range(m):
    trains.append([0]*n)
for i in range(n):
    stations.append([0]*n)
    g[i]=[]
direction=[]
for i in range(m):
    b = list(map(int, input().split()))
    c=b.pop(0)
    if len(b)>2:
        if b[0]>b[2]:
            direction.append(-1)
        else:
            direction.append(1)
    else:
        direction.append(1)
    for j in range(c):
        trains[i][b[2*j]-1]=b[2*j+1]
    for j in range(c-1):
        g[b[2*j]-1].append(b[2*j+2]-1)
        stations[b[2*j]-1][b[2*j+2]-1]=1
timecount=0
ways=[]
for i in range(m):
    if trains[i][e-1]!=0:
        ways.append(trains[i][e-1])

def dijkstra(graph,sv,ev):
    dist=[]
    for j in range(n):
        dist.append(9**9)
    dist[sv]=0
    visited=set()
    queue=[sv]
    while queue:
        v=queue.pop(0)
        for u in graph[v]:
            if dist[u]==9**9:
                dist[u]=dist[v]+1
                queue.append(u)
        visited.add(v)
    return dist[ev]


def tryway(graph,ways):
    while ways:
        m=min(ways)
        if dijkstra(graph,0,e-1)==9**9:
            ways.remove(m)
            continue
        else:
            return m
    return -1
print(tryway(g,ways))
