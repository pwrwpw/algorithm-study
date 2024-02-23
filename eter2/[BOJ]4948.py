array = [True for i in range(1234567)]
array[1] = False

for i in range(2, 1234567):
    if array[i]:
        j = 2
        while i * j < 1234567:
            array[i * j] = False
            j += 1

while True:
    n = input()
    n = int(n)
    
    if n == 0:
        break
    
    cnt = 0
    for i in range(n+1, 2*n+1):
        if array[i]:
            cnt += 1
    
    print(cnt)