# 모든 순열
from itertools import permutations


number = [x for x in range(1,int(input())+1)]

for i in permutations(number):
    print(*list(i))
