# 백준 2750번 : 수 정렬하기(https://www.acmicpc.net/problem/2750)
# 버블정렬을 이용한 방식

data = []

n = int(input())
for a in range(n) : 
    data.append(int(input()))

for i in range(len(data)) : #패스(i번째 기준)
    for j in range(len(data) - (1+i)) : #비교횟수
        if (data[j] > data[j+1]) : 
            data[j], data[j+1] = data[j+1], data[j]

for i in range(len(data))   :         
    print(data[i])