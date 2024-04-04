from collections import deque

N = int(input())
graph = []
maxNum = 0

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,value,visited):

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
result = 0

for i in range(maxNum):
    visited = [ [0]*N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i,visited)
                cnt +=1

    if result < cnt:
        result = cnt

print(result)