
n = int(input())

arr = list(map(int,input().split()))
answer = 0
def is_prime(value):
    if value < 2:
        return False
    for i in range(2,int(value**0.5)+1):
        if value % i == 0:
            return False
    return True

for j in arr:
    if is_prime(j):
        answer += 1

print(answer)