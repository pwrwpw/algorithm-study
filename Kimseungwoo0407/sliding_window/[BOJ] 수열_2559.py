N, K = map(int,input().split())

temp = list(map(int,input().split()))

value = sum(temp[:K])

max_value = value

for i in range(K,N):
    value += temp[i]
    value -= temp[i-K]

    if value > max_value:
        max_value = value

print(max_value)