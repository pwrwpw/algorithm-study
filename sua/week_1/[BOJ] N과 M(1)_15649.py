#아직 백트래킹 알고리즘에 익숙하지않고 이해가 안가서 파이썬 내장함수를 사용했습니다!

import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()