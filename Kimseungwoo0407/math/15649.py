# n과 m
from itertools import permutations

n,m = map(int,input().split())

list = [x for x in range(1,n+1)]

if m == 1:
    for i in list:
        print(i)

else:
    for i in permutations(list,m):
        print(' '.join(map(str,i)))