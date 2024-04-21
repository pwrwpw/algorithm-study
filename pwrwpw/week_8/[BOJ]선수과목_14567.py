import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

in_degree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1

levels = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
        levels[i] = 1

result = []
while q:
    now = q.popleft()
    result.append(now)

    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)
            levels[next] = levels[now] + 1

print(*levels[1::])