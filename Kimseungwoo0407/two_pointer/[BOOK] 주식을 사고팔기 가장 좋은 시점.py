array = [7, 1, 5, 3, 6, 4]

min_price = float('inf')  # 가능한 가장 큰 값으로 초기화
max_profit = 0

for i in array:
    profit = i - min_price

    # 최대 이익 업데이트
    max_profit = max(max_profit, profit)

    # 최소 가격 업데이트
    min_price = min(min_price, i)

print(max_profit)
