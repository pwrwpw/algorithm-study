from collections import Counter
import sys

n = int(input())

data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()
mean = round(sum(data)/len(data))
median = data[len(data)//2]

frequency = Counter(data)



most_common_frequency = frequency.most_common()


max_frequency = most_common_frequency[0][1]
modes = [num for num, freq in most_common_frequency if freq == max_frequency]

if len(modes) > 1:
    mode = sorted(modes)[1]
else:
    mode = modes[0]

print(mean)
print(median)
print(mode)
print(max(data)-min(data))