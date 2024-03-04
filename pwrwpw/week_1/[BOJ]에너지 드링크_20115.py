# 시간복잡도 : NlogN

n = int(input())

drinks = list(map(int,input().split()))

drinks.sort()

while len(drinks) != 1:
    a = drinks.pop()
    b = drinks.pop()
    max_value,min_value = max(a,b),min(a,b)
    drinks.append(max_value + (min_value / 2))

print('%g'%drinks[0])