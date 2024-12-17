a = list(map(int, input().split()))
queue = list(map(int, input().split()))
quantity=a[0]
k=a[1]
num=0
clients=[0]*k
t=0
while queue[-1]!=0:
    for i in range(k):
        if clients[i]==0 and queue[-1]!=0:
            clients[i]=queue[num]
            queue[num]=0
            num+=1
    for i in range(k):
        clients[i]-=1
    t+=1
print(t+max(clients))