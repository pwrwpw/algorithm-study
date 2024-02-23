# n과 m(2)

# 오름차순의 조합

from itertools import combinations

n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for comb in combinations(lst, m):
    print(' '.join(map(str, comb)))