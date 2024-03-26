N, X = map(int, input().split())

visiter = list(map(int, input().split()))

if max(visiter) == 0:
    print('SAD')
else:
    value = sum(visiter[:X])

    max_value = value

    max_cnt = 1

    for i in range(X, N):
        value += visiter[i]

        value -= visiter[i - X]

        if value > max_value:
            max_value = value
            max_cnt = 1

        elif value == max_value:
            max_cnt += 1
    print(max_value)
    print(max_cnt)