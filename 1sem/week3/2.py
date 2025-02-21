n=int(input())
n1=n
z=0
if n==abs(n):
    z=''
else:
    z='-1*'
if n1==0:
    z=0
m=[]
i=2
while i<=abs(n):
    if n%(i)==0:
        m.append(i)
        n=n/i
    else:
        i+=1
k=[]
j=0
while j<len(m):
    k1=m.count(m[j])
    if k1>1:
        for i in range(k1-1):
            m.remove(m[j])
    k.append(k1)
    j+=1
print(n1,'=',z, sep='',end='')
for i in range(len(m)):
    print('(',m[i],'^',k[i],')', sep='',end='')
    if i<len(m)-1:
        print('*',end='')