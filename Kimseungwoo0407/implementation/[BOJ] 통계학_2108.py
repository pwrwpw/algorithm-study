from collections import Counter
import sys

n = int(input())

data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()
mean = round(sum(data)/len(data))
median = data[len(data)//2]
a = Counter(data).most_common(2)
mode = a[0][0]
if len(a) > 1 and a[0][1] == a[1][1]:
    mode = a[1][0]
print(mean)
print(median)
print(mode)
print(max(data)-min(data))