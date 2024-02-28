# 시간복잡도 : NlogN

n = int(input())

tips = []
for _ in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)
tip = 0

for i in range(n):
    customer_tip = tips[i] - i
    if customer_tip < 0:
        break
    tip += customer_tip

print(tip)