#g=[]
#n=int(input())
#for i in range(n):
#    g.append(list(map(int,input().split())))

g=[[0,0,0,2],
    [1,0,0,4],
    [0,0,0,2],
    [1,0,3,0]]
gr=[[0, 1, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0]]
n=len(gr[0])

def dijkstra(graph,sv,ev):
    dist=[]
    for j in range(n):
        dist.append(9**9)
    dist[sv]=0
    visited=set()
    while len(visited)<n:
        dist2=[]
        for k in range(n):
            if k not in visited:
                dist2.append(dist[k])
            else:
                dist2.append(9**9)
        v=dist2.index(min(dist2))
        for u in range(n):
            if u not in visited and graph[v][u]!=0:
                if dist[u]>dist[v]+graph[v][u]:
                    dist[u]=dist[v] + graph[v][u]
        visited.add(v)
    return dist[ev]

print(dijkstra(gr,1,3))