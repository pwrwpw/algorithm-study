N = int(input())

arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    for j in i:
        print(j, end=' ')
    print()