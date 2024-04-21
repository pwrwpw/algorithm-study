N = int(input())

a,b = map(int,input().split())

M = int(input())

graph = [ [] for _ in range(N+1)]

visited = [False] * (N+1)

count = 0

result = []

for i in range(M):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(a,count):
    count += 1

    if a == b:
        result.append(count)

    for i in graph[a]:
        if not visited[i]:
            visited[i] = True
            dfs(i,count)

dfs(a,count)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)