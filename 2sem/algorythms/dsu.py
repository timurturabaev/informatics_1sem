def makeset(s,x):
    s.append([x])

def find(s,x):
    for i in range(len(s)):
        if x in s[i]:
            return i
    return None

def union(s,x,y):
    xs = find(s,x)
    ys = find(s,y)
    if xs==ys:
        return
    else:
        small=min(xs,ys)
        big=max(xs,ys)
        for el in s[big]:
            s[small].append(el)
        s.remove(s[big])

s=[]
makeset(s,0)
makeset(s,3)
print(find(s,0),find(s,4))
print(s[0])
union(s,0,3)
print(s[0])