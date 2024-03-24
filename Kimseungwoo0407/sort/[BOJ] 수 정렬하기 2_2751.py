import sys
input=sys.stdin.readline

num = int(input())
result =[]

for _ in range(num):
    result.append(int(input()))

for i in sorted(result):
    print(i)