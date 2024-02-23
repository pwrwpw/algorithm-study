from itertools import combinations

n, k = map(int, input().split())
n = [i+1 for i in range(n)]
ans = combinations(n, k)
for a in ans:
    print(*a) #a의 각 요소를 개별적으로 출력