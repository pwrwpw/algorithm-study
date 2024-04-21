N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

result = {}

for i in a:
    result[i] = 1

for j in b:
    if j not in result:
        print(0, end = ' ')
    else:
        print(1, end = ' ')
