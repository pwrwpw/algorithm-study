n = int(input())

x,y = map(int,input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

def dfs(x,num):
    num +=1
    visited[x] = True

    if x == y:
        result.append(num)
    for i in graph[x]:
        if not visited[i]:
            dfs(i,num)

dfs(x,0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)