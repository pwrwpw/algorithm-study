n, m = map(int, input().split()) 
listA = []
for a in range(n): 
    listA.append(list(map(int, list(input()))))
listB = []
for b in range(n): 
    listB.append(list(map(int, list(input()))))


def rev(i, j): 
    for x in range(i, i+3):
        for y in range(j, j+3):
            if listA[x][y] == 0:
                listA[x][y] = 1
            else:
                listA[x][y] = 0


cnt = 0 
if (n < 3 or m < 3) and listA != listB:
    # 예외 
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                rev(r, c)

if cnt != -1:
    if listA != listB:
        cnt = -1
print(cnt)