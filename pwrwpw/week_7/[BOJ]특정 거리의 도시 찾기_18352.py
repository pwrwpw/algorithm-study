import heapq
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for idx in graph[now]:
            cost = 1 + dist
            if cost < distance[idx]:
                distance[idx] = cost
                heapq.heappush(queue, (cost, idx))


dijkstra(x)

flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        flag = True
        print(i)
if not flag:
    print(-1)
