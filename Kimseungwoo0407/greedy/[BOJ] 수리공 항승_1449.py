N, L = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 물이 새는 위치를 정렬

count = 0
start = 0

for i in data:
    if start < i:
        start = i + L - 1
        count += 1

print(count)