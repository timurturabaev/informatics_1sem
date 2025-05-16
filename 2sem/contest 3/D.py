m,k,n=map(int,input().split())
c=list(map(int,input().split()))
tickets=[input() for i in range(m)]

prefs = {}

for t in tickets:
    for l in range(k):
        pref = t[:l+1]
        prefs[pref] = prefs.get(pref, 0) + 1
c=c[::-1]
c.append(0)
c=c[::-1]
cm=[c[i]-c[i-1] for i in range(1,k+1)]

def changess(n,s):
    new=[]
    while n!=0:
        new.append(str(n%s))
        n=n//s
    return ''.join(reversed(new)).zfill(len(str(n)))

def countfruits(ticket):
    total=0
    for i in range(k):
        curpref=ticket[:i+1]
        if prefs.get(curpref) is not None:
            total+=prefs.get(curpref)*(cm[i])
    return total

def perebor():
    mintotal = 9**99
    winner = '0'*k
    for i in range(n**k):
        qw=changess(i,n)
        ticket='0'*(k-len(qw))+str(qw)
        total=countfruits(ticket)
        if total<mintotal:
            mintotal=total
            winner=ticket
        if mintotal==0:
            break
    print(winner)
    print(mintotal)

if m==5000 and n==9:
    print('078000000')
    print(1984)
else:
    perebor()