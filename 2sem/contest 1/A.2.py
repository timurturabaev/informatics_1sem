a=list(map(int,input().split()))
ne,m=a[0],a[1]
def psod(x):
    r=x
    l=len(str(x))
    for i in range(l):
        r+=x%10
        x-=x%10
        x/=10
    return r

def log(x,n):
    c=0
    while n**c<x:
        c+=1
    return c

s=4

def dijkstra(graph,sv,ev):
    dist=[]
    for j in range(s):
        dist.append(9**5)
    dist[sv]=0
    visited=set()
    while len(visited)<1000:
        dist2=[]
        for k in range(s):
            if k not in visited:
                dist2.append(dist[k])
            else:
                dist2.append(9**5)
        v=dist2.index(min(dist2))
        for u in range(s):
            if u not in visited:
                if dist[u]>dist[v]+graph[v][u]:
                    dist[u]=dist[v] + graph[v][u]
        visited.add(v)
    return dist[ev]

graph=[]
for i in range(s):
    graph.append([9**5]*s)
queue=[ne]
vis=[ne]
i=0
while m not in queue:
    x=queue.pop(0)
    if int(x-2) not in vis and int(x-2)>=0:
        queue.append(int(x-2))
        graph[x][x-2] = 1
    if int(x*3) not in vis and int(x*3)<=9999:
        queue.append(int(x*3))
        graph[x][x*3] = 1
    if int(psod(x)) not in vis and int(psod(x))<=9999:
        queue.append(int(psod(x)))
        graph[x][psod(x)]=1
    print(graph)
    vis.append(int(x))
print(dijkstra(graph,ne,m))