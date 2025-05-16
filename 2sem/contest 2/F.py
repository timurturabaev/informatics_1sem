n,k = map(int, input().split())
g=[]
gt=[]
patience=[[k]*2*n]
for j in range(n):
    z = input()
    x = []
    for i in z:
        x.append(int(i))
    g.append(x)
    gt.append(x.copy())
for i in range(n):
    for j in range(n):
        gt[i][j]=g[j][i]
q=9**99
for i in range(n):
    if sum(g[i])<q:
        q=sum(g[i])
    if sum(gt[i])<q:
        q=sum(gt[i])
y=q+k
if y<n:
    print(y)
else:
    print(n)