N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]

visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    if visited[x] == 0:
        visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
    return sum(visited) - 1


print(dfs(1))