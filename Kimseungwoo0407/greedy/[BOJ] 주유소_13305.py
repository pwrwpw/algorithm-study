N = int(input())
distance = list(map(int,input().split()))
costs = list(map(int,input().split()))

min_cost = 1000000001

result = 0

city = 0

for cost in costs:
    if min_cost > cost:
        min_cost = cost
    result += min_cost * distance[city]
    if city < len(distance)-1:
        city+=1
    else:
        break

print(result)