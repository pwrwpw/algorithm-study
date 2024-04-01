def quick_sort_reverse(arr, low, high):
    if low < high:
        pi = partition_reverse(arr, low, high)
        quick_sort_reverse(arr, low, pi - 1)
        quick_sort_reverse(arr, pi + 1, high)

def partition_reverse(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

multi = []
plus = []
minus = []


zero_count = arr.count(0)
for num in arr:
    if num > 1:
        multi.append(num)
    elif num == 1:
        plus.append(num)
    else:
        minus.append(num)

quick_sort_reverse(multi,0,len(multi)-1)
quick_sort(minus,0,len(minus)-1)

answer = sum(plus)

for i in range(0, len(multi), 2):
    if i+1 >= len(multi):
        answer += multi[i]
    else:
        answer += (multi[i] * multi[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        answer += minus[i]
    else:
        answer += (minus[i] * minus[i+1])

print(answer)
