# 시간복잡도 : O(NlogN)

import sys
n = int(input())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lectures_state = []

for start, end in lectures:
    lectures_state.append((start, 1))
    lectures_state.append((end, -1))

lectures_state.sort()

count = 0
max_count = 0

for _, state in lectures_state:
    count += state
    max_count = max(max_count, count)

print(max_count)