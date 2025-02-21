o=1
s=0
p=1
f = open('input.txt')
n = [float(x) for x in f.readline().split()]
a = f.readline()
f.close
if a == '+':
    for i in range(len(n)):
        s+=n[i]
    o=s
elif a == '*':
    for i in range(len(n)):
        p*=n[i]
    o=p
elif a == '-':
    v=n[0]
    for i in range(len(n)):
        v-=n[i]
    v+=n[0]
    o=v
else:
    o='error'
f = open('output.txt', 'w')
f.write(str(o))
f.close
