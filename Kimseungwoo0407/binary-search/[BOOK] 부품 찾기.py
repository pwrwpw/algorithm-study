def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
things = list(map(int, input().split()))
things.sort()

M = int(input())
want = list(map(int, input().split()))

for target in want:
    if binary_search(things, 0, len(things), target):
        print('yes', end=' ')
    else:
        print('no', end=' ')