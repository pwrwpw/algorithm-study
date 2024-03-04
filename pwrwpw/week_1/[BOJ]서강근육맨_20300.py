#시간 복잡도: NlogN

n = int(input())

healthy = list(map(int,input().split()))

healthy.sort()

answer = []

if n % 2 == 1:
    answer.append(healthy[-1])
    healthy = healthy[:-1]

for i in range(len(healthy) // 2):
    answer.append(healthy[i] + healthy[len(healthy)-1-i])
print(max(answer))