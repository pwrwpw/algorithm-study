import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr += list(map(int, sys.stdin.readline().split()))

min_time = int(1e9)
min_height = 0
    
for i in range(257):
    plus = 0
    minus = 0
    
    for j in arr:
        if j > i:
            plus += j - i
        else:
            minus += i - j
            
    if plus + b < minus:
        continue
    
    tmp_time = plus * 2 + minus
    
    if tmp_time <= min_time:
        min_height = i
        min_time = tmp_time
        
print(min_time, min_height)