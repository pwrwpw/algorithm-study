import sys

n,m = map(int,sys.stdin.readline().split())

titles = [sys.stdin.readline().split() for _ in range(n)]

scores = [int(sys.stdin.readline()) for _ in range(m)]

for score in scores:
    right = len(titles)
    left = 0
    temp = 0
    while left <= right:
        mid = (right+left) // 2
        if int(titles[mid][1]) >= score:
            temp = mid
            right = mid - 1
        else:
            left = mid + 1
    print(titles[temp][0])