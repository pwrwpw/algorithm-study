# 시간복잡도 : 0(1)

n = int(input())

cnt = 0
while True:
    if n % 5 != 0:
        n -= 2
        cnt += 1
    else:
        cnt += n // 5
        print(cnt)
        break
    if n < 0:
        print("-1")
        break