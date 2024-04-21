N,M = map(int,input().split())

arr = list(map(int,input().split()))

start, end = 0, 1

count = 0

while end < N+1:
    arr_sum = sum(arr[start:end])
    if arr_sum > M:
        start +=1
    elif arr_sum < M:
        end +=1
    else:
        count +=1
        start+=1

print(count)