#comb 사용
from math import comb
n, m = map(int, input().split())
print(comb(n, m))

#nCm = n!/m! = n!/m!(n-m!) 이용한 for문
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, m = map(int, input().split())
print(fact(n) // (fact(n-m) * fact(m)))  # n!/m!(n-m!)
