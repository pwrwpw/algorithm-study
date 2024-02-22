import sys

max_limit = 1000000

is_prime = [True] * (max_limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i+i, max_limit + 1, i):
            is_prime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3,n//2+1,2):
        if is_prime[i] and is_prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
        if n - i <= 0:
            print("Goldbach's conjecture is wrong.")
            break
