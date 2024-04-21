v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
for edge in edges:
    a, b, cost = edge

    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)