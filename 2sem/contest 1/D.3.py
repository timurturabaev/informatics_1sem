a=list(map(int,input().split()))
n, m ,k = a[0],a[1],a[2]
for i in range(m):
    b = list(map(int, input().split()))
s = [0]*k
for i in range(k):
    c = list(input().split())
    s[i] = [c[0],c[1],c[2]]
s=s[::-1]
answer=[]
graph = [i for i in range(1, n + 1)]
t = [0] * n

def search(s, k):
    if s[k-1] != k:
        s[k-1] = search(s, s[k-1])
    return s[k-1]

def add(graph, t, x, y):
    x = search(graph, x)
    y = search(graph, y)
    if x == y:
        return
    if t[x-1] == t[y-1]:
        t[x-1] += 1
    if t[x-1] < t[y-1]:
        graph[x - 1] = y
    else:
        graph[y - 1] = x

for i in range(k):
    s[i][1]=int(s[i][1])
    s[i][2]=int(s[i][2])
    if s[i][0] == 'cut':
        add(graph,t,s[i][1],s[i][2])
    else:
        if search(graph,s[i][1])==search(graph,s[i][2]):
            answer.append('YES')
        else:
            answer.append('NO')
answer=answer[::-1]
for i in range(len(answer)):
    print(answer[i])
