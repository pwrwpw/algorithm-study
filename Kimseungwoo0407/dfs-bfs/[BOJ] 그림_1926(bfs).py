from collections import deque
n,m = map(int,input().split())

visited = [ [False] * m for _ in range(n)]

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []
def bfs(x,y):
    count = 1

    queue = deque()
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    count +=1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            a = bfs(i,j)
            result.append(a)

if len(result) == 0:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))