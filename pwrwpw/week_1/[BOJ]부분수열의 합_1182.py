"""

combinations 를 이용한 풀이

from itertools import combinations

n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0

for i in range(1,n+1):
    coms = combinations(arr,i)

    for com in coms:
        if sum(com) == s:
            cnt += 1

print(cnt)
"""

n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def count_combinations(i, total):
    global count

    if i == n:
        return
    count_combinations(i + 1, total)
    if total + arr[i] == s:
        count += 1
    count_combinations(i + 1, total + arr[i])

count_combinations(0, 0)
print(count)