A = list(map(int, input().split()))
B = A.copy()
for i in range(len(A)):
    s = A[i]
    while s >= 10:
        k = s
        s = 0
        while k >= 1:
            s += k % 10
            k = k // 10
    B[i] = s
l = len(B)

w=1
while w>0:
    w=0
    for i in range(l-1):
        if B[i]>B[i+1]:
            B[i],B[i+1]=B[i+1],B[i]
            A[i], A[i + 1] = A[i + 1], A[i]
            w+=1
w=1
while w>0:
    w=0
    for i in range(l-1):
        if A[i]>A[i+1] and B[i]==B[i+1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            w+=1
for i in range(l):
    print(A[i], end=' ')