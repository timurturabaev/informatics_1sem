a=[]
n=int(input())
for i in range(n):
    a.append(list(map(int,input().split())))

def dijkstra(graph,sv,ev):
    dist=[9*99 for in range(n)]
    prev=[None for i in range(n)]
    dist[sv]=0
    q=set()
    while len(q)<n:
        v=dist.index(min(dist))
