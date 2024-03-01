n, m = input().split()
n = int(n)
m = int(m)

array = [True for i in range(m + 1)]
array[1] = False

for i in range(2, m + 1):
    if array[i] == True:
        j = 2
        while i * j < m + 1:
            array[i * j] = False
            j += 1

for i in range(n, m + 1):
    if (array[i]):
        print(i)