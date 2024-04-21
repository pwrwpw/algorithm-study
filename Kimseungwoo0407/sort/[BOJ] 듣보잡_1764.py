N, M = map(int, input().split())

no_listen = set()

no_look = set()

for _ in range(N):
    no_listen.add(input())

for _ in range(M):
    no_look.add(input())

result = []

for i in no_listen:
    if i in no_look:
        result.append(i)

result.sort()

print(len(result))

for i in result:
    print(i)
