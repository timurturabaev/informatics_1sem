a=list(map(int,input().split()))
n, m ,k = a[0],a[1],a[2]
g = dict()
for i in range(n):
    g[i]=[]
for i in range(m):
    b = list(map(int, input().split()))
s = [0]*k

def dfsvisit(graph,nod,nod2):
    color=[0 for p in g]
    stack = [nod]
    while stack:
        node = stack.pop(-1)
        color[node] = 1
        for neighbour in graph[node]:
            if neighbour==nod2:
                return True
            if color[neighbour] == 0:
                stack.append(neighbour)
    return False

for i in range(k):
    c = list(input().split())
    s[i] = [c[0],c[1],c[2]]
s=s[::-1]
answer=[]
for i in range(k):
    if s[i][0] == 'cut':
        g[int(s[i][1])-1].append(int(s[i][2])-1)
        g[int(s[i][2])-1].append(int(s[i][1])-1)
    else:
        if dfsvisit(g,int(s[i][1])-1,int(s[i][2])-1):
            answer.append('YES')
        else:
            answer.append('NO')
answer=answer[::-1]
for i in range(len(answer)):
    print(answer[i])