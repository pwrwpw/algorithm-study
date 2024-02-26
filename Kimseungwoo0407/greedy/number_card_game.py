

import sys

# 표준 입력을 빠르게 받기 위해 sys.stdin.readline() 사용
# N, M을 공백으로 구분하여 입력받음
n, m = map(int, sys.stdin.readline().split())

# 최종 결과를 저장할 변수 초기화
result = 0

# N번 반복하여 각 행의 데이터를 입력받음
for _ in range(n):
    # 현재 행의 데이터를 공백으로 구분하여 입력받음
    li = list(map(int, sys.stdin.readline().split()))

    # 현재 행에서 가장 작은 수를 찾음
    a = min(li)

    # 지금까지 찾은 행의 최소값들 중 가장 큰 값을 result에 저장
    result = max(result, a)

# 최종 결과 출력
print(result)