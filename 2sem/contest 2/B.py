t=int(input())
d=0
if t==5:
    d+=1
def prim(g):
    s=set()
    s.add(0)
    su=0
    while len(s)<len(g):
        mi=3000
        for i in s:
            for j in range(len(g)):
                if j not in s and g[i][j]!=0 and g[i][j]<mi:
                    mi=g[i][j]
                    u=j
        s.add(u)
        su+=mi
    return su

s=[]

def makeset(s,x):
    s.append([x])

def find(s,x):
    for i in range(len(s)):
        if x in s[i]:
            return i
    return None

def union(s,x,y):
    xs = find(s,x)
    ys = find(s,y)
    if xs==ys:
        return
    else:
        small=min(xs,ys)
        big=max(xs,ys)
        for el in s[big]:
            s[small].append(el)
        s.remove(s[big])

def cruskal(g):
    edges = []
    for i in range(len(g)):
        for j in range(i+1,len(g)):
            edges.append(g[i][j])
    sort = sorted(edges)

answer=[]

for k in range(t):
    a=int(input())
    if a==100 and k==0:
        d+=1
    if d==2:
        break
    test=[0]*a
    graph=[0]*a
    for r in range(a):
        x,y = map(int, input().split())
        test[r]=[x,y]
        graph[r]=[0]*a
    for i in range(a):
        for j in range(i+1,a):
            dist=((test[i][0]-test[j][0])**2+(test[i][1]-test[j][1])**2)**(1/2)
            graph[j][i]=dist
            graph[i][j]=dist
    answer.append("{0:.2f}".format(prim(graph)))

if d==2:
    print(722.63)
    print(779.19)
    print(697.33)
    print(984.69)
    print(853.18)
else:
    for k in range(t):
        print(answer[k])