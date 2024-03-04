n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x : (x[1],x[0]))

end_time = 0
count = 0


for i in data:
    start, end = i
    if start >= end_time:
        end_time = end
        count += 1

print(count)