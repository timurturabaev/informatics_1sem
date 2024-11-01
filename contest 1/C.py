n=int(input())
a=list(map(int, input().split()))
if sum(a)%3==0 and max(a)<=(sum(a)/3):
    print(1)
else:
    print(0)