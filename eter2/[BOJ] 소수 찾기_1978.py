n = input()
n = int(n)
nums = [int(x) for x in input().split()]

array = [True for i in range(1001)]
array[1] = False

for i in range(2, 1001):
    if array[i] == True:
        j = 2
        while i * j < 1001:
            array[i * j] = False
            j += 1

cnt = 0
for i in nums:
    if array[i]:
        cnt += 1

print(cnt)