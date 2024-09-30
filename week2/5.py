a = input().split()
a[1:], a[0] = a[:-1], a[-1]
print(' '.join(map(str, a)))