N=int(input())
b=int(input())
c=int(input())
a=[]
k=0
e=0
while N//(10**k)>=1:
    k+=1
while k>=0:
    e+=(N//(10**(k-1)))*(b**(k-1))
    N=N%(10**(k-1))
    k-=1
while e>=c:
    a.append(int(e%c))
    e=e//c
a.append(int(e))
d=a[::-1]

print(''.join(map(str,d)))