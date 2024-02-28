

def is_prime(value):
    if value < 2:
        return False
    for j in range(2,int(value**0.5) + 1):
        if value % j == 0:
            return False
    return True

m,n = map(int,input().split())

for i in range(m,n+1):
    if is_prime(i):
        print(i)