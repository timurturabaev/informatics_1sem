a=input().split()
n=int(a[0])
s=a[1]
l=len(s)
k=int(l/n)
b=[]
for i in s:
    b.append(i)
for i in range(n):
    d=b[i*k:(i+1)*k]
    print(''.join(map(str, d[::-1])),end='')