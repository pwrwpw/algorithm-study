# 소인수분해

number = int(input())
n = 2

while True:
    if number == 1:
        break
    if number % n == 0:
        number //= n
        print(n)
    else:
        n+=1
