n = int(input())
roads = list(map(int,input().split()))
price = list(map(int,input().split()))

total = 0

min_value = price[0]
total += roads[0] * price[0]
for i in range(1,n-1):
    min_value = min(price[i],min_value)
    total += roads[i] * min_value

print(total)