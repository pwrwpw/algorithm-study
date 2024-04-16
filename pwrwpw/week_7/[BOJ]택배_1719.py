n, m = map(int, input().split())

distance = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

graph = [[i for i in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0
    graph[i][i] = '-'

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)
    distance[b][a] = min(distance[b][a], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                graph[i][j] = graph[i][k]
for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end = ' ')
    print()