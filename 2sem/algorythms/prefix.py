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
    return p
s='abaabac'
print(prefix(s))