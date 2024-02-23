n, m = input().split()
n = int(n)
m = int(m)

def func(arr):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n + 1):
        if i in arr:
            continue
        arr.append(i)
        func(arr)
        arr.pop()

for i in range(n):
    func([i + 1])