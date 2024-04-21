# 못생긴 수
n = int(input())

d = [0] * n

d[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    d[l] = min(next2, next3, next5)

    if d[l] == next2:
        i2 += 1
        next2 = d[i2] * 2
    if d[l] == next3:
        i3 += 1
        next3 = d[i3] * 3
    if d[l] == next5:
        i5 += 1
        next5 = d[i5] * 5

print(d[n - 1])