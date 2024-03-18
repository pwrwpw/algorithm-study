def dfs(v):
    visited[v] = True
    for nx in networks[v]:
        if not visited[nx]:
            dfs(nx)

c = int(input())
v = int(input())

networks = [[] for _ in range(c+1)]
visited = [False] * (c+1)

for _ in range(v):
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

dfs(1)

total_connection = sum(visited) - 1

print(total_connection)
