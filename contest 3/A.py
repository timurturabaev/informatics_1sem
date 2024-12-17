a = list(map(int, input().split()))
b = list(map(int, input().split()))
n=a[0]
k=a[1]

t=1
while t**t<len(b):
    t+=1
def qminsearch(x):
    l=len(x)
    if l<=t:
        return min(x)
    x1=[]
    for i in range(l//t-1):
        x1.append(min(x[i*t:(i+1)*t]))
    x1.append(min(x[l//t-1:l]))
    return qminsearch(x1)
for i in range(k):
    c=qminsearch(b)
    print(c,end=' ')
    b.remove(c)