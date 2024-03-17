from collections import deque

def bfs(x, cnt):
    queue = deque()

    queue.append((x, cnt))
    visited[x] = 1

    while queue:
        x, cnt = queue.popleft()
        visited[x] = 1

        if (x == k):
            return cnt

        for nx in [2 * x, x - 1, x + 1]:
            if 0 <= nx <= 100000:
                if visited[nx] == 0:
                    if nx == 2 * x:
                        queue.append((nx, cnt))
                    else:
                        queue.append((nx, cnt + 1))

n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n, 0))