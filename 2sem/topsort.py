graph = {0:[1,4],1:[2,3],2:[3],3:[0],4:[1],5:[4]}

def dfsvisit(graph,node,color,visited):
    color[node]=1
    visited.append(node)
    for neighbour in graph[node]:
        if color[neighbour]==0:
            dfsvisit(graph,neighbour,color,visited)
    color[node]=2

def dfs(graph):
    components = []
    color = [0 for i in graph]
    for node in graph:
        if color[node]==0:
            visited = []
            dfsvisit(graph,node,color,visited)
            components.append(visited)
        return components

def tsvisit(graph,node,color,ts):
    color[node]=1
    for neighbour in graph[node]:
        if color[neighbour]==0:
            tsvisit(graph,neighbour,color,ts)
    color[node]=2
    ts.insert(0,node)

def topsort(graph):
    color = [0 for i in graph]
    ts = []
    for node in graph:
        if color[node]==0:
            tsvisit(graph,node,color,ts)
    return ts


def kosaraju(graph):
    ts = topsort(graph)
    graph_t = {node: [] for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            graph_t[neighbour].append(node)
    color = [0 for i in graph]
    while ts:
        node = ts[0]
        component = []
        dfsvisit(graph_t,node,color,component)
        print(component)
        for node in component:
            ts.remove(node)

kosaraju(graph)
