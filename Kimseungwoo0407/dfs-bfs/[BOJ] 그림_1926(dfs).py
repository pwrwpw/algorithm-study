import sys
sys.setrecursionlimit(10**6)
n, m = map(int,input().split())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
result = 0

def dfs(x,y):
    if x < 0 or x >= n or y >= m or y <0:
        return False
    if data[x][y] == 1:
        global count
        count +=1
        data[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

ans = []

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
                result +=1
                ans.append(count)
                count = 0

if result == 0:
    print(0)
    print(0)

else:
    print(result)
    print(max(ans))