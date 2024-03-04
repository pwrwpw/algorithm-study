n = int(input())

arr = []
for _ in range(n):
  a, b = map(int, input().split())
  arr.append([a, b])

arr.sort(key = lambda x: (x[1], x[0]))

ans = 0
end = 0

for a, b in arr:
  if a >= end:
    ans += 1
    end = b

print(ans)