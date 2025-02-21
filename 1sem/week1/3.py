b=1
A = list(map(float, input().split()))
for i in range(len(A)):
    b*=A[i]
print(b**(1/(len(A))))