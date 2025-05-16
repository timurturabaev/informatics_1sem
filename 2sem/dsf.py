def find(s, k):
    if s[k-1] != k:
        s[k-1] = find(s, s[k-1])
    return s[k-1]

def union(s, t, x, y):
    x = find(s, x)
    y = find(s, y)
    if x == y:
        return
    if t[x-1] == t[y-1]:
        t[x-1] += 1
    if t[x-1] < t[y-1]:
        s[x-1] = y
    else:
        s[y-1] = x

n, m, k = map(int, input().split())
graph = [i for i in range(1, n + 1)]
rank = [0] * n
for _ in range(m):
    input()
operations = [input() for _ in range(k)]
operations = reversed(operations)

answers = []
for op in operations:
    action, x, y = op.split()
    x, y = int(x), int(y)

    if action == 'ask':
        answers.insert(0, 'YES' if find(graph, x) == find(graph, y) else 'NO')
    
    if action == 'cut':
        union(graph, rank, x, y)

print('\n'.join(answers))
