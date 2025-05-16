l=int(input())
t=input()
r=input()
x=r+'#'+t+'1'+t
y=r+'#'+t+'0'+t
def prefix(s):
    n = len(s)
    p = [0]*n
    for i in range(1,n):
        k = p[i-1]
        while k>0 and s[k]!=s[i]:
            k = p[k-1]
        if s[k]==s[i]:
            k+=1
        p[i]=k
        if p[i]==l-1:
            return i-l+1
a=prefix(x)
b=prefix(y)
if a is None:
    if b is None:
        print('Random')
    else:
        if y[b]=='1':
            print('Yes')
        else:
            print('No')
elif b is None:
    if x[a] == '1':
        print('Yes')
    else:
        print('No')
else:
    if x[a]==y[b]=='1':
        print('Yes')
    elif x[a]==y[b]=='0':
        print('No')
    else:
        print('Random')

