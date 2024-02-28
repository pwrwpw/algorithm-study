import sys

A, B = map(int,sys.stdin.readline().split())
count = 1

while A != B:
    if B % 10 == 1:
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count +=1
    else:
        count = -1
        break
    if A > B:
        count = -1
        break

if count == -1:
    print(-1)
else:
    print(count)