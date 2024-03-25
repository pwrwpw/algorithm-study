A, B = map(int,input().split())

A_arr = list(map(int,input().split()))
B_arr = list(map(int,input().split()))

result = sorted(A_arr+B_arr)

for i in result:
    print(i, end =' ')