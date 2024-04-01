n = int(input())
k = int(input())

min_value = 1
max_value = n * n
answer = 0

while min_value <= max_value:
    mid = (min_value + max_value) // 2
    count = sum(min(mid // i, n) for i in range(1, n + 1))

    if count >= k:
        answer = mid
        max_value = mid - 1
    else:
        min_value = mid + 1

print(answer)
