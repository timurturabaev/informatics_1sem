f = open('input.txt')
a = f.read()
s = 0
s += a.count('.')
s += a.count('!')
s += a.count('?')
s -= a.count('...')*2
s -= a.count('!?')
s -= a.count('?!')
print(s)