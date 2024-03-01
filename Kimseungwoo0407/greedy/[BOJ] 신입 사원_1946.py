import sys

T = int(sys.stdin.readline())  # 2

for test_case in range(T):
    N = int(sys.stdin.readline())
    data = []
    for number in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))

    data.sort()

    count = 1
    min_rank = data[0][1]

    for i in range(1, N):
        if data[i][1] < min_rank:
            min_rank = data[i][1]
            count += 1
    print(count)