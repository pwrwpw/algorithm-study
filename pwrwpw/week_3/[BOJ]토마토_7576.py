from collections import deque

n, m = map(int,input().split())

tomatos = [list(map(int,input().split())) for _ in range(m)]

queue = deque([])

for i in range(m):
    for j in range(n):
        if tomatos[i][j] == 1:
            queue.append([i,j])

def bfs():
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append([nx,ny])

bfs()
answer = 0
for tomato in tomatos:
    for state in tomato:
        if state == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(tomato))

print(answer-1)