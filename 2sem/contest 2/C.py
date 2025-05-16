t=int(input())

def kuhn(graph,l):
    match = [0] * (n+m+1)
    visited = [False] * (n+m+1)
    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == 0 or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in l:
        visited = [False] * (n+m+1)
        if dfs(v):
            max_matching += 1
    return max_matching

answer=[]

for i in range(t):
    n,m,p = map(int,input().split())
    graph = dict()
    for q in range(1,n+1):
        graph[q]=[w for w in range(n+1,n+m+1)]
    for q in range(n+1,n+m+1):
        graph[q]=[w for w in range(1,n+1)]
    miss=list(map(int,input().split()))
    for k in range(p):
        graph[miss[2*k]+1].remove(miss[2*k+1]+n+1)
        graph[miss[2*k+1]+n+1].remove(miss[2*k]+1)
    l=[w for w in range(1,n+1)]
    answer.append(kuhn(graph,l))

for i in range(t):
    print(answer[i])