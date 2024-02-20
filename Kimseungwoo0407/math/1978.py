# 소수 찾기


n = int(input())

m = list(map(int,input().split()))

result = 0

for i in m:
    count = 0
    if i == 1:
        continue
    if i == 2:
        result += 1

    else:
        for j in range(1,i+1):
            if i % j == 0:
                count +=1
        if count == 2:
            result +=1

print(result)