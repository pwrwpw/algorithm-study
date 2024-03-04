from itertools import combinations

while True:
    arr = list(map(int,input().split()))
    k = arr[0]
    s = arr[1:]
    if k == 0:
        break
    a = list(combinations(s,6))
    for i in a:
        for j in range(len(i)):
            print(i[j],end=" ")
        print("")
    print("")