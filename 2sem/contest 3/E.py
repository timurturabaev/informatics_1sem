n=int(input())
ws=[]
for i in range(n):
    a=input()
    ws.append(a)
pairs=[]

def ispal(s):
    return s==s[::-1]

for i in range(n):
    for j in range(n):
        if i!=j and ispal(ws[i]+ws[j]):
            pairs.append((i+1,j+1))
print(len(pairs))
for i in range(len(pairs)):
    print(pairs[i][0],pairs[i][1])