def z(t,u):
    s=t+'#'+u
    n=len(s)
    zf = [0]*n
    left,right = 0, 0
    for i in range(1,n):
        zf[i]=max(0,min(right-i,zf[i-left]))
        while i+zf[i]<n and s[zf[i]]==s[i+zf[i]]:
            zf[i]+=1
        if i+zf[i]>right:
            left=i
            right=i+zf[i]
    return zf

u='tralalerotralala'
t='rot'
print(z(t,u))