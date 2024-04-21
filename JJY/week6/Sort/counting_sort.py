# 백준 2750번 : 수 정렬하기(https://www.acmicpc.net/problem/10989)
# 계수정렬을 이용한 방식 
# -> 출현하는 숫자의 범위가 작고, 반복적으로 나온다면 계수정렬!

data = []

n = int(input())
for a in range(n) : 
    data.append(int(input()))
    
bucket = [0] * (max(data)+1)

for i in range(len(data)) :
    bucket[data[i]] += 1 # 각 양동이에 적힌 인덱스의 값 증가 (count)
    
for i in range(len(bucket)) :
    if bucket[i] == 0 :
        continue
    else : 
        for j in range(bucket[i]):
            print (i)
            
            
            
# import sys
# n = int(input())

# array = [0 for _ in range(10001)] 

# for _ in range(n):
#     num = int(sys.stdin.readline())
#     array[num] += 1

# for i in range(1,10001):
#     count = array[i]
#     for _ in range(count):
#         print(i)