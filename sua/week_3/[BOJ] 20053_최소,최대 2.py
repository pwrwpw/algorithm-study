n = int(input())

for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    print(min(arr),max(arr))

#다른 풀이

for _ in range(int(input())):
    N = int(input())
    li = sorted(map(int, input().split()))
print(li[0], li[-1])