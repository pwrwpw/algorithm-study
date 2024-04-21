N = int(input())

graph = [ list(map(int,input())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    global count
    if graph[x][y] == 1:
        count +=1
        graph[x][y] = 0

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                dfs(nx,ny)
count = 0
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(count)
            count=0

print(len(result))
result.sort()
for i in result:
    print(i)