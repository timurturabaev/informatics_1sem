f = open('input.txt')
q=[]
for line in f:
    q.append(line)
b=[]
d=[]
for i in q[2]:
    v=int(i)
    break
for i in q[1]:
    w=i
    break
x=0
for i in q[0]:
    if i=='0' or i=='1' or i =='2' or i=='3' or i=='4' or i =='5' or i=='6' or i=='7' or i =='8' or i=='9':
        if x==0:
            b.append(i)
        else:
            d.append(i)
    else:
        x+=1
b1=''.join(map(str,b))
d1=''.join(map(str,d))
b2=int(b1)
d2=int(d1)
def fun(N,s,c):
    a=[]
    k = 0
    e = 0
    while N // (10 ** k) >= 1:
        k += 1
    while k >= 0:
        e += (N // (10 ** (k - 1))) * (s ** (k - 1))
        N = N % (10 ** (k - 1))
        k -= 1
    while e >= c:
        a.append(int(e % c))
        e = e // c
    a.append(int(e))
    y = a[::-1]
    return int(''.join(map(str, y)))
b3=fun(b2, v, 10)
d3=fun(d2, v, 10)
if w=='+':
    z=d3+b3
if w=='-':
    z=d3-b3
if w=='*':
    z=d3*b3
print(fun(z,10,v))