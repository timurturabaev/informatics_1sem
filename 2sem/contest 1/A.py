a=list(map(int,input().split()))
n,m=a[0],a[1]
def psod(x):
    r=x
    l=len(str(x))
    for i in range(l):
        r+=x%10
        x-=x%10
        x/=10
    return r

def log(x,n):
    c=0
    while n**c<x:
        c+=1
    return c

queue=[n]
vis=[[n]]
b=[0]
s=1
v=[]
while m not in queue:
    for j in range(k):
        if m not in queue:
            if queue[0]-2 not in vis:
                queue.append(queue[0]-2)
                vis.append(queue[0] - 2)
                b
            if queue[0]*3 not in vis and queue[0]*3<=9999 and queue[0]>0:
                queue.append(queue[0]*3)
                vis.append(queue[0]*3)
                k+=1
            if psod(queue[0]) not in vis and psod(queue[0])<=9999 and queue[0]>0:
                queue.append(psod(queue[0]))
                vis.append(psod(queue[0]))
                k+=1
            queue.remove(queue[0])
            print(vis)
            print(queue)
print(vis.index(vis[-1]))
