# 로또

from itertools import combinations

while True:
    n = list(map(int,input().split()))
    if n[0] == 0:
        break
    else:
        n = n[1:]

    for i in combinations(n,6):
        print(*i)
    print()
