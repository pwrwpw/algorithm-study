T = int(input())

for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    ans = 0

    max = 0
    for i in range(len(price)-1, -1, -1):
        if price[i] > max:
            max = price[i]
        else:
            ans += max - price[i]

    print(ans)