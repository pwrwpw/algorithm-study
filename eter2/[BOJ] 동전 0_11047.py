n, k = map(int, input().split())

arr = []
for _ in range(n):
  a = int(input())
  arr.append(a)

arr = sorted(arr, reverse=True)

ans = 0
for a in arr:
  if k - a >= 0:
    ans += k // a
    k = k % a

print(ans)