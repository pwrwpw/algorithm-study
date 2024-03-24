n = int(input())
f_li = set(map(int,input().split()))
m = int(input())
s_li = list(map(int,input().split()))

for i in s_li:
    if i not in f_li:
        print(0)
    else:
        print(1)