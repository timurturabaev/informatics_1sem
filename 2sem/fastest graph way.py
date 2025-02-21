graph=[]
n=int(input())
for i in range(n):
    graph.append(list(map(int,input().split())))

def newedges(g):
    b=0
    graph=g.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][j]!=0 and graph[j][k]!=0:
                    if graph[i][j]+graph[j][k]<graph[i][k] or graph[i][k]==0:
                        graph[i][k]=graph[i][j] + graph[j][k]
                        b+=1
    if b==0:
        return graph
    return newedges(graph)


def r(graph,sv,ev):
    graph = newedges(graph)
    if graph[sv][ev] != 0:
        return graph[sv][ev]
    return 'infinity'

s=int(input('start:'))
e=int(input('end:'))
print(r(graph,s,e))