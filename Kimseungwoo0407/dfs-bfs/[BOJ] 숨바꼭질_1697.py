from collections import deque

N, K = map(int, input().split())

visited = [float('inf')] * 100001

move = [-1, 1, 2]

def bfs(N, K):
    queue = deque()
    queue.append(N)
    visited[N] = 0
    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]

        for i in move:
            if i != 2:
                nx = x + i
            else:
                nx = x * i

            if 0 <= nx < 100001 and visited[nx] > visited[x] + 1:
                visited[nx] = visited[x] + 1
                queue.append(nx)


print(bfs(N, K))