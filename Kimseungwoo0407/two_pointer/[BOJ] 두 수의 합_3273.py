N = int(input())

arr = list(map(int, input().split()))
X = int(input())

arr.sort()

left, right = 0, len(arr) - 1

count = 0

while left < right:
    if arr[left] + arr[right] > X:
        right -= 1
    elif arr[left] + arr[right] < X:
        left += 1
    else:
        count += 1
        right -= 1
        left += 1

print(count)