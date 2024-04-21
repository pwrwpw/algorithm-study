from collections import deque

def solve(h):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > h:
                bfs(i,j,h)
                cnt +=1
    return cnt

def bfs(x,y,h):
    queue = deque()
    queue.append((x,y))
    v[x][y] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if v[nx][ny] == 0 and arr[nx][ny] > h:
                    queue.append((nx,ny))
                    v[nx][ny] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0

for h in range(100):
    v = [ [0] * N for _ in range(N)]
    ans = max(ans,solve(h))

print(ans)