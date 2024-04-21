N = int(input())
M = int(input())

armor = list(map(int,input().split()))

count = 0
left = 0
right = N-1

armor.sort()

while left < right :
    sum_num = armor[left] + armor[right]

    if sum_num < M:
        left+=1
    elif sum_num > M:
        right-=1
    else:
        count +=1
        left+=1
        right-=1

print(count)

