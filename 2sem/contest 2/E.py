t=int(input())
graph = {1:[2,3,4,6],2:[1,3],3:[1,2,4,6],4:[3,5],5:[4,6],6:[1,3,5,7],7:[6],8:[]}
def bfs(graph,sv,ev):
    dist=[]
    for j in range(len(graph)+1):
        dist.append(999)
    dist[sv]=0
    visited=set()
    queue=[sv]
    while queue:
        v=queue.pop(0)
        for u in graph[v]:
            if u not in visited:
                if dist[u]>dist[v]+1:
                    dist[u]=dist[v]+1
                visited.add(u)
                queue.append(u)
    return dist[ev]
#print(bfs(graph,5,3))
def otvet(g,rc,tc,p):
    shortcut=[]
    travel=[]
    for robot in rc:
        h=p
        dest=[]
        ways = []
        for destination in tc:
            if bfs(g,robot,destination)!=999:
                ways.append(bfs(g,robot,destination))
                dest.append(destination)
            else:
                h-=1
        if h<0:
            return -1
        travel.append([ways,dest])
    c=1
    while c>0:
        c=0
        for i in range(len(rc)):
            for j in range(i+1,len(rc)):
                a=travel[i][0].index(min(travel[i][0]))
                b = travel[j][0].index(min(travel[j][0]))
                if travel[i][1][a]==travel[j][1][b]:
                    c+=1
                    if b>a:
                        travel[i][0].remove(travel[i][0][a])
                        travel[i][1].remove(travel[i][1][a])
                    else:
                        travel[j][0].remove(travel[j][0][b])
                        travel[j][1].remove(travel[j][1][a])
    for i in range(len(rc)):
        shortcut.append(min(travel[i][0]))
    return max(shortcut)

ans=[]

for i in range(t):
    p=0
    rc=[]
    tc=[]
    g=dict()
    g[0]=[]
    x,y = map(int,input().split())
    s=[]
    z = input()
    for k in range(1, y):
        n = k
        g[n] = []
        if z[k] != 'X' and z[k - 1] != 'X':
            g[n].append(n - 1)
            g[n - 1].append(n)
        if z[k] == 'R':
            rc.append(n)
            p-=1
        elif z[k] == 'T':
            tc.append(n)
            p+=1
    s.append(z)
    for j in range(1,x):
        z=input()
        n=j*y
        g[n]=[]
        if z[0] != 'X' and s[j - 1][0] != 'X':
            g[n].append(n - y)
            g[n - y].append(n)
        if z[0] == 'R':
            rc.append(n)
            p-=1
        elif z[0] == 'T':
            tc.append(n)
            p+=1
        for k in range(1,y):
            n=j*y+k
            g[n]=[]
            if z[k]!='X' and z[k-1]!='X':
                g[n].append(n-1)
                g[n-1].append(n)
            if z[k]!='X' and s[j-1][k]!='X':
                g[n].append(n-y)
                g[n-y].append(n)
            if z[k]=='R':
                rc.append(n)
                p-=1
            elif z[k]=='T':
                tc.append(n)
                p+=1
        s.append(z)
    ans.append(otvet(g,rc,tc,p))

for i in ans:
    print(i)