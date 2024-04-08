from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(v):
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N,M,V = map(int,input().split())

graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)