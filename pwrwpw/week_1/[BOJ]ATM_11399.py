# 시간복잡도 : NlogN

n = int(input())

peoples = list(map(int,input().split()))

peoples.sort()

total = 0
idx = 0
for i in peoples:
    idx += i
    total += idx

print(total)