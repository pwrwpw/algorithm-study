# 시간복잡도 : NlogN
n = int(input())

products = []

for _ in range(n):
    products.append(int(input()))

products.sort(reverse=True)

price = 0
for i in range(2,n,3):
    price += products[i]

print(sum(products) - price)