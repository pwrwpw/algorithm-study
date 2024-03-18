from collections import deque

n, m = map(int,input().split())

mazes = [list(map(int,input())) for _ in range(n)]

def bfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if mazes[nx][ny] == 0:
                continue

            if mazes[nx][ny] == 1:
                mazes[nx][ny] = mazes[x][y] + 1
                queue.append((nx, ny))
    return mazes[n-1][m-1]

print(bfs(0, 0))