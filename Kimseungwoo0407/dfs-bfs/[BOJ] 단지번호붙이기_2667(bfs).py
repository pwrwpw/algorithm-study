from collections import deque

def bfs(x,y):
    global count
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == 1:
            graph[x][y] = 0
            count += 1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<N and 0 <= ny < N and graph[nx][ny] == 1:
                    queue.append((nx,ny))

N = int(input())

graph = [ list(map(int,input())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []
count = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i,j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)
