import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parents = [i for i in range(n)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(n):
    connections = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if connections[j] == 1:
            union(i, j)

plan = list(map(int, sys.stdin.readline().split()))
plan = [x - 1 for x in plan]

is_connected = all(find(plan[0]) == find(city) for city in plan)

if is_connected:
    print("YES")
else:
    print("NO")
