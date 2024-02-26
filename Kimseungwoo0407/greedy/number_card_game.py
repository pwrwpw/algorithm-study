n,m = map(int,input().split())

result = 0

for _ in range(n):
    li = list(map(int,input().split()))
    a = min(li)
    result = max(result,a)

print(result)