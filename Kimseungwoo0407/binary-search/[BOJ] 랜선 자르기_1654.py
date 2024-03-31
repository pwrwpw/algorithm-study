K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    count = sum(lan // mid for lan in lans)

    if count < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
